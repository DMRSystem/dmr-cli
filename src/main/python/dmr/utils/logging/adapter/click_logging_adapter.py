
from ..logging_adapter import ILoggingAdapter

import click


class ClickLoggingAdapter(ILoggingAdapter):

    def info(self, message):
        click.echo(message)
