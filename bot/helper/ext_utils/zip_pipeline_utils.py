import os
from contextlib import suppress
from asyncio import create_subprocess_exec
from asyncio.subprocess import PIPE
from os import path as ospath, walk
from re import search as re_search, I

from ... import LOGGER, cores, threads
from ...core.config_manager import BinConfig
from .bot_utils import cmd_exec, sync_to_async
from .files_utils import get_path_size, clean_target
from .media_utils import get_document_type
from ..mirror_leech_utils.status_utils.zip_pipeline_status import ZipPipelineStatus
from ... import task_dict, task_dict_lock

async def merge_videos(video_files, output_path, listener):
    """
    Merges video files using ffmpeg concat.
    """
    from ... import cpu_eater_lock
    list_file = ospath.join(listener.dir, "concat_list.txt")
    async with cpu_eater_lock:
        with open(list_file, 'w') as f:
            for file in video_files:
                f.write(f"file '{file}'\n")

        cmd = [
            "taskset", "-c", f"{cores}",
            BinConfig.FFMPEG_NAME, "-hide_banner", "-loglevel", "error",
            "-f", "concat", "-safe", "0", "-i", list_file,
            "-c", "copy", "-threads", f"{threads}", output_path
        ]

        if listener.is_cancelled:
            return False

        listener.subproc = await create_subprocess_exec(*cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = await listener.subproc.communicate()
        code = listener.subproc.returncode

        if os.path.exists(list_file):
            os.remove(list_file)

        if code != 0:
            err = stderr.decode().strip()
            LOGGER.error(f"FFmpeg concat failed: {err}")
            return False
        return True

async def merge_binary(files, output_path, listener):
    """
    Merges files by binary concatenation.
    """
    try:
        if listener.is_cancelled:
            return False

        # Use cat for speed
        files_str = " ".join([f'"{f}"' for f in files])
        cmd = f'cat {files_str} > "{output_path}"'
        _, stderr, code = await cmd_exec(cmd, True)

        if code != 0:
            LOGGER.error(f"Binary merge failed: {stderr}")
            return False
        return True
    except Exception as e:
        LOGGER.error(f"Error in merge_binary: {e}")
        return False

async def zip_pipeline_process(listener, dl_path):
    """
    Main Zip Pipeline logic: Detect, Extract, Merge.
    """
    # 1. Extraction is already handled if listener.extract is True

    # 2. Merge Stage
    async with task_dict_lock:
        task_dict[listener.mid] = ZipPipelineStatus(listener, listener.mid)
    # Search for mergeable files
    mergeable_videos = []
    mergeable_splits = []

    video_extensions = ('.mp4', '.mkv', '.avi', '.ts', '.mov')
    split_extensions = ('.part1', '.part01', '.part001', '.001')

    for dirpath, _, files in await sync_to_async(walk, dl_path):
        # We only merge files in the same directory
        v_parts = [ospath.join(dirpath, f) for f in files if f.lower().endswith(video_extensions)]
        s_parts = [ospath.join(dirpath, f) for f in files if any(f.lower().endswith(ext) for ext in split_extensions) or re_search(r'\.part\d+$', f.lower())]

        if len(v_parts) > 1:
            v_parts.sort()
            mergeable_videos.append((dirpath, v_parts))

        if len(s_parts) > 1:
            s_parts.sort()
            # Verify they are parts of the same file
            # Simple check: same base name before .part
            # This is complex, but for now let's group by base name
            groups = {}
            for p in s_parts:
                base = re_search(r'(.*?)\.part\d+$|(.*?)\.\d+$', ospath.basename(p))
                if base:
                    bname = base.group(1) or base.group(2)
                    if bname not in groups: groups[bname] = []
                    groups[bname].append(p)
            for bname, parts in groups.items():
                if len(parts) > 1:
                    mergeable_splits.append((dirpath, bname, parts))

    # Perform Merges
    merged_any = False

    # Merge Splits first
    for dirpath, bname, parts in mergeable_splits:
        LOGGER.info(f"ZipPipeline: Merging split files for {bname}")
        out_name = bname
        output_path = ospath.join(dirpath, out_name)
        if await merge_binary(parts, output_path, listener):
            for p in parts:
                await clean_target(p)
            merged_any = True
            # Re-check if this merged file is a video and can be merged with others
            if out_name.lower().endswith(video_extensions):
                # Update mergeable_videos if necessary (advanced)
                pass

    # Merge Videos
    for dirpath, parts in mergeable_videos:
        # Re-verify parts still exist
        parts = [p for p in parts if os.path.exists(p)]
        if len(parts) <= 1: continue

        LOGGER.info(f"ZipPipeline: Merging video files in {dirpath}")
        # Use first part's name as base
        base_name = ospath.basename(parts[0])
        # Remove part indication from name if possible
        clean_name = re_search(r'(.*?)(?:\.part\d+|_part\d+|[-_]\d+)?\.\w+$', base_name)
        if clean_name:
            out_name = f"MERGED_{clean_name.group(1)}{ospath.splitext(base_name)[1]}"
        else:
            out_name = f"MERGED_{base_name}"

        output_path = ospath.join(dirpath, out_name)
        if await merge_videos(parts, output_path, listener):
            for p in parts:
                await clean_target(p)
            merged_any = True

    return merged_any
