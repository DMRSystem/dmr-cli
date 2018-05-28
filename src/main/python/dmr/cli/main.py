import click

from .command.setup import setup


@click.group()
def main():
    pass


main.add_command(setup)
