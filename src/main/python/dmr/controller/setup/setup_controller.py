
from .setup_behavior import SetupBehavior
from .platform_adapter import PlatformAdapter
from typing import Dict


class SetupController(object):

    def __init__(self, **kwargs):
        self.setup_behaviors: Dict[str, SetupBehavior] = {}
        self.platform_adapter: PlatformAdapter = kwargs['platform_adapter']

    def add_setup_behavior(self, setup_behavior: SetupBehavior) -> None:
        system_name: str = setup_behavior.get_system_name()
        self.setup_behaviors[system_name] = setup_behavior

    def do_setup(self) -> None:
        system_name: str = self.platform_adapter.get_system()
        self._check_behavior_defined_for_system(system_name)
        self.setup_behaviors[system_name].do_setup()

    def _check_behavior_defined_for_system(self, system_name: str) -> None:
        if system_name not in self.setup_behaviors:
            raise Exception('Behavior not defined for system name: {}', system_name)

