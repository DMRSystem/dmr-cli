
from dmr.controller.setup.setup_behavior import SetupBehavior


class OSXSetupBehavior(SetupBehavior):

    def get_system_name(self) -> str:
        return 'Darwin'
