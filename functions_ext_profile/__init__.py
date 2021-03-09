import os
import gc
from psutil import Process
from logging import Logger
from azure.functions import FuncExtensionBase, Context


class ProfileExtension(FuncExtensionBase):

    def __init__(self, filename: str):
        super().__init__(filename)
        self.pid: int = os.getpid()
        self.process: Process = Process(self.pid)

        self.io_read_start = None
        self.io_write_start = None
        self.io_read_bytes_start = None
        self.io_write_bytes_start = None

    def before_invocation(self, logger: Logger, context: Context, *args, **kwargs) -> None:
        counter = self.process.io_counters()
        self.io_read_start = counter.read_count
        self.io_write_start = counter.write_count
        self.io_read_bytes_start = counter.read_bytes
        self.io_write_bytes_start = counter.write_bytes

    def after_invocation(self, logger: Logger, context: Context, *args, **kwargs) -> None:
        counter = self.process.io_counters()
        io_read_end = counter.read_count
        io_write_end = counter.write_count
        io_read_bytes_end = counter.read_bytes
        io_write_bytes_end = counter.write_bytes

        logger.warn(f'{context.function_name} Stats: '
                    f'[IO Read/Write Count {io_read_end - self.io_read_start}/{io_write_end - self.io_write_start}] '
                    f'[IO Read/Write Bytes {io_read_bytes_end - self.io_read_bytes_start}/{io_write_bytes_end - self.io_write_bytes_start}]')