from time import time
from .... import LOGGER
from ...ext_utils.status_utils import (
    get_readable_file_size,
    MirrorStatus,
    EngineStatus,
    get_readable_time,
)

class ZipPipelineStatus:
    def __init__(self, listener, gid):
        self.listener = listener
        self._gid = gid
        self._start_time = time()
        self.engine = EngineStatus().STATUS_FFMPEG

    def gid(self):
        return self._gid

    def progress(self):
        return "0%"

    def speed(self):
        return "0B/s"

    def processed_bytes(self):
        return "0B"

    def name(self):
        return self.listener.name

    def size(self):
        return get_readable_file_size(self.listener.size)

    def eta(self):
        return "-"

    def status(self):
        return MirrorStatus.STATUS_MERGING

    def task(self):
        return self

    async def cancel_task(self):
        LOGGER.info(f"Cancelling Zip Pipeline (Merge): {self.listener.name}")
        self.listener.is_cancelled = True
        if (
            self.listener.subproc is not None
            and self.listener.subproc.returncode is None
        ):
            try:
                self.listener.subproc.kill()
            except:
                pass
        await self.listener.on_upload_error("Zip Pipeline (Merge) stopped by user!")
