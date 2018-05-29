
from ..logging_adapter import ILoggingAdapter

import click


class ClickLoggingAdapter(ILoggingAdapter):

    def info(self, message, color: str = None, indentation: int = 0):
        message = self._add_correct_indentation(message, indentation)
        click.secho(message, fg=color)

    def _add_correct_indentation(self, message: str, indentation: int):
        return '    '*indentation + ('\n'+'    '*indentation).join(message.split('\n'))
