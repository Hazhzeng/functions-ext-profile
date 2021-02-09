from typing import Dict
from logging import Logger
from azure.functions import FuncExtension, Context
from psutil import virtual_memory


class ProfileExtension(FuncExtension):

    def __init__(self, filename: str):
        super().__init__(filename)
        self.memory_case: Dict[str, float] = {}

    def before_invocation(self, logger: Logger, context: Context, *args, **kwargs) -> None:
        mem = virtual_memory()
        self.memory_case[context.function_name] = mem.percent
        return super().before_invocation(logger, context, *args, **kwargs)

    def after_invocation(self, logger: Logger, context: Context, *args, **kwargs) -> None:
        mem = virtual_memory()
        memory_utiliazation = mem.percent - self.memory_case[context.function_name]
        del self.memory_case[context.function_name]
        logger.info(f'{context.function_name} used memory percentage {memory_utiliazation}%')
        return super().after_invocation(logger, context, *args, **kwargs)