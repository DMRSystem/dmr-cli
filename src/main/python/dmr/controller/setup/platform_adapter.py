import platform

class PlatformAdapter(object):

    def get_system(self) -> str:
        return platform.system()