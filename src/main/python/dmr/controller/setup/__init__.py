
import dependency_injector.providers as providers

from dmr.controller.setup.setup_controller import SetupController
from dmr.controller.setup.platform_adapter import PlatformAdapter
from dmr.controller.setup.setup_behavior import SetupBehavior
from dmr.controller.setup.behavior.osx.step.mixxx_downloader import MixxxDownloader
from dmr.utils.logging.adapter.click_logging_adapter import ClickLoggingAdapter
from dmr.utils.requests.requests_adapter import RequestsAdapter


class SetupControllerProvider(providers.Provider):

    def __call__(self, *args, **kwargs):

        download_url = 'http://python-dependency-injector.ets-labs.org/index.html'
        download_directory = '/Users/connorboyle/Downloads'
        logging_adapter = ClickLoggingAdapter()
        requests_adapter = RequestsAdapter()

        mixxx_downloader = MixxxDownloader(download_url=download_url,
                                           logging_adapter=logging_adapter,
                                           download_directory=download_directory,
                                           requests_adapter=requests_adapter)

        osx_setup_behavior = SetupBehavior('Darwin')
        osx_setup_behavior.add_setup_step(mixxx_downloader)

        platform_adapter = PlatformAdapter()
        setup_controller = SetupController(platform_adapter=platform_adapter)
        setup_controller.add_setup_behavior(osx_setup_behavior)

        return setup_controller


class SetupControllerModule(providers.Singleton):
    setup_controller = SetupControllerProvider()
