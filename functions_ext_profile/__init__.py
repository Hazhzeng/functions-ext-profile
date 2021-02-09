import os
import gc
from psutil import Process
from logging import Logger
from azure.functions import FuncExtension, Context


class ProfileExtension(FuncExtension):

    def __init__(self, filename: str):
        super().__init__(filename)
        self.pid: int = os.getpid()
        self.process: Process = Process(self.pid)
        self.mem_start = None

        self.io_read_start = None
        self.io_write_start = None
        self.io_read_bytes_start = None
        self.io_write_bytes_start = None

        gc.disable()

    def before_invocation(self, logger: Logger, context: Context, *args, **kwargs) -> None:
        gc.collect()
        self.mem_start = self.process.memory_info().rss

        counter = self.process.io_counters()
        self.io_read_start = counter.read_count
        self.io_write_start = counter.write_count
        self.io_read_bytes_start = counter.read_bytes
        self.io_write_bytes_start = counter.write_bytes

    def after_invocation(self, logger: Logger, context: Context, *args, **kwargs) -> None:
        mem_end = self.process.memory_info().rss

        counter = self.process.io_counters()
        io_read_end = counter.read_count
        io_write_end = counter.write_count
        io_read_bytes_end = counter.read_bytes
        io_write_bytes_end = counter.write_bytes

        logger.info(f'{context.function_name} Stats: '
                    f'[Memory Usage {mem_end - self.mem_start} bytes] '
                    f'[IO Read/Write Count {io_read_end - self.io_read_start}/{io_write_end - self.io_write_start}] '
                    f'[IO Read/Write Bytes {io_read_bytes_end - self.io_read_bytes_start}/{io_write_bytes_end - self.io_write_bytes_start}]')