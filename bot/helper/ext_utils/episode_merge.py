import os
import re
from asyncio import create_subprocess_exec
from asyncio.subprocess import PIPE
from os import path as ospath, walk
from re import search as re_search, findall, I

from ... import LOGGER, cores, threads, task_dict, task_dict_lock
from ...core.config_manager import BinConfig, Config
from .bot_utils import cmd_exec, sync_to_async
from .files_utils import get_path_size, clean_target
from ..mirror_leech_utils.status_utils.zip_pipeline_status import ZipPipelineStatus
from .status_utils import MirrorStatus, EngineStatus

class EpisodeMergeStatus:
    def __init__(self, listener, gid, status="Merging"):
        self.listener = listener
        self._gid = gid
        self._status = status
        self.engine = EngineStatus().STATUS_FFMPEG

    def gid(self):
        return self._gid

    def progress(self):
        return "0%"

    def speed(self):
        return "-"

    def name(self):
        return self.listener.name

    def size(self):
        return "N/A"

    def eta(self):
        return "-"

    def status(self):
        if self._status == "Sorting":
            return MirrorStatus.STATUS_SORTING
        return MirrorStatus.STATUS_MERGING

    def task(self):
        return self

    async def cancel_task(self):
        self.listener.is_cancelled = True
        if self.listener.subproc:
            try:
                self.listener.subproc.kill()
            except:
                pass

def extract_episode_number(filename):
    # Common patterns for episode numbers
    patterns = [
        r'[Ss]\d+[Ee](\d+)',         # S01E01
        r'[Ee]p(?:isode)?\.?\s*(\d+)', # Episode 01, Ep.01, Ep 01
        r'[Ee](\d+)\b',               # E01
        r'\b(\d+)\s*(?:v\d+)?\s*(?:\[|\()', # 01 [720p] or 01 (10bit)
        r'-\s*(\d+)\b',               # - 01
    ]
    for pattern in patterns:
        match = re_search(pattern, filename, I)
        if match:
            return int(match.group(1))

    # Last resort: find any numbers that look like episodes
    numbers = findall(r'\b\d+\b', filename)
    if numbers:
        # Usually the last number before extension if it's not a year
        for num in reversed(numbers):
            if 0 < int(num) < 2000: # Simple heuristic to avoid years
                return int(num)
    return None

def extract_season_number(filename):
    patterns = [
        r'[Ss](\d+)[Ee]\d+',         # S01E01
        r'[Ss]eason\s*(\d+)',        # Season 1
        r'[Ss](\d+)\b',              # S1
    ]
    for pattern in patterns:
        match = re_search(pattern, filename, I)
        if match:
            return int(match.group(1))
    return 1 # Default to Season 1

def extract_show_name(filename):
    # Try to get everything before S01E01 or Season 1
    patterns = [
        r'(.*?)\s*-\s*[Ss]\d+',
        r'(.*?)\s*[Ss]\d+',
        r'(.*?)\s*-\s*[Ee]p',
        r'(.*?)\s*[Ee]p',
        r'(.*?)\s*-\s*\d+',
    ]
    for pattern in patterns:
        match = re_search(pattern, filename, I)
        if match:
            name = match.group(1).strip()
            if name: return name

    # Fallback to base name without extension and common junk
    name = ospath.splitext(filename)[0]
    name = re.sub(r'\[.*?\]|\(.*?\)', '', name).strip()
    return name

async def episode_merge_process(listener, dl_path):
    if not (Config.ENABLE_AUTO_MERGE or Config.MERGE_EPISODES):
        return False

    async with task_dict_lock:
        task_dict[listener.mid] = EpisodeMergeStatus(listener, listener.mid, "Sorting")

    video_extensions = ('.mp4', '.mkv', '.avi')
    video_files = []

    for dirpath, _, files in await sync_to_async(walk, dl_path):
        for f in files:
            if f.lower().endswith(video_extensions) and not any(x in f.lower() for x in ['sample', 'extra', 'trailer']):
                video_files.append(ospath.join(dirpath, f))

    if len(video_files) <= 1:
        return False

    # 1. Sorting Stage
    LOGGER.info(f"EpisodeMerge: Sorting {len(video_files)} files in {dl_path}")

    # We might want to update status here
    # Since I can't easily import everything without circular deps,
    # I'll just use ZipPipelineStatus for now as a placeholder or implement a new one

    episodes = []
    for f in video_files:
        ep_num = extract_episode_number(ospath.basename(f))
        if ep_num is not None:
            episodes.append((ep_num, f))
        else:
            LOGGER.warning(f"EpisodeMerge: Could not find episode number for {f}")
            # Keep it but it might be out of order
            episodes.append((999, f))

    episodes.sort(key=lambda x: x[0])
    sorted_files = [x[1] for x in episodes]

    # 2. Merge Stage
    async with task_dict_lock:
        task_dict[listener.mid] = EpisodeMergeStatus(listener, listener.mid, "Merging")

    from ... import cpu_eater_lock

    # Generate output name
    first_file = ospath.basename(sorted_files[0])
    show_name = extract_show_name(first_file)
    season_num = extract_season_number(first_file)

    first_ep = episodes[0][0] if episodes[0][0] != 999 else 1
    last_ep = episodes[-1][0] if episodes[-1][0] != 999 else len(episodes)

    ext = ospath.splitext(first_file)[1]
    output_name = f"{show_name} - Season {season_num} (Episodes {first_ep:02d}–{last_ep:02d}){ext}"
    output_path = ospath.join(dl_path, output_name)

    LOGGER.info(f"EpisodeMerge: Merging into {output_name}")

    list_file = ospath.join(dl_path, "concat_list.txt")
    try:
        with open(list_file, 'w', encoding='utf-8') as f:
            for file_path in sorted_files:
                # ffmpeg requires escaped single quotes in file paths for concat
                escaped_path = file_path.replace("'", "'\\''")
                f.write(f"file '{escaped_path}'\n")

        cmd = [
            "taskset", "-c", f"{cores}",
            BinConfig.FFMPEG_NAME, "-hide_banner", "-loglevel", "error",
            "-f", "concat", "-safe", "0", "-i", list_file,
            "-c", "copy", "-threads", f"{threads}", output_path
        ]

        if listener.is_cancelled:
            return False

        async with cpu_eater_lock:
            listener.subproc = await create_subprocess_exec(*cmd, stdout=PIPE, stderr=PIPE)
            stdout, stderr = await listener.subproc.communicate()
            code = listener.subproc.returncode

        if code != 0:
            err = stderr.decode().strip()
            LOGGER.error(f"FFmpeg episode merge failed: {err}")
            if ospath.exists(output_path):
                os.remove(output_path)
            return False

        # Cleanup original files
        for f in sorted_files:
            await clean_target(f)

        if ospath.exists(list_file):
            os.remove(list_file)

        return True
    except Exception as e:
        LOGGER.error(f"Error in episode_merge: {e}")
        return False
    finally:
        if ospath.exists(list_file):
            with suppress(Exception): os.remove(list_file)
