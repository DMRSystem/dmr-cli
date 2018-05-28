
from ..logging_adapter import ILoggingAdapter

import click


class ClickLoggingAdapter(ILoggingAdapter):

    def info(self, message, color=None):
        click.echo(click.style(message, fg=color))
