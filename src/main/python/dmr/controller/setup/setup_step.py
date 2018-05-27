
class ISetupStep(object):

    def execute(self) -> None:
        raise NotImplementedError()
