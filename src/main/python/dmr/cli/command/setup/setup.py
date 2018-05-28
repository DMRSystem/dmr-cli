
import click
from dmr.utils.pass_controller import pass_controller
from dmr.controller.setup import SetupControllerModule, SetupController


def dummy_provider():
    return 'Hello'


@click.command()
@pass_controller(injector=SetupControllerModule.setup_controller)
def setup(setup_controller: SetupController):
    setup_controller.do_setup()



