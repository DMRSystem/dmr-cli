
import dependency_injector.providers as providers

from dmr.controller.setup.setup_controller import SetupController
from dmr.controller.setup.platform_adapter import PlatformAdapter
from dmr.controller.setup.setup_behavior import SetupBehavior
from dmr.controller.setup.behavior.osx.step.mixxx_downloader import MixxxDownloader, AlreadyDownloadedCheckDecorator
from dmr.controller.setup.behavior.osx.step.mixxx_download_mounter import MixxxDownloadMounter
from dmr.controller.setup.behavior.osx.step.mixxx_download_remover import MixxxDownloadRemover
from dmr.utils.logging.adapter.click_logging_adapter import ClickLoggingAdapter
from dmr.utils.requests.requests_adapter import RequestsAdapter
from pathlib import Path


class SetupControllerProvider(providers.Provider):

    def __call__(self, *args, **kwargs):

        download_url = 'https://downloads.mixxx.org/mixxx-2.1.0/mixxx-2.1.0-osxintel.dmg'
        download_file_path = Path(Path.home(), '.dmr', 'temp')
        progress_bar_color = 'green'
        download_file_name = download_url.rsplit('/', 1)[-1]
        full_download_path = Path(download_file_path, download_file_name)
        logging_adapter = ClickLoggingAdapter()
        requests_adapter = RequestsAdapter(progress_bar_color)

        mixxx_downloader = MixxxDownloader(download_url=download_url,
                                           logging_adapter=logging_adapter,
                                           download_file_path=download_file_path,
                                           download_file_name=download_file_name,
                                           requests_adapter=requests_adapter)

        mixxx_downloader = AlreadyDownloadedCheckDecorator(mixxx_downloader,
                                                           full_download_path,
                                                           logging_adapter)

        mixxx_download_mounter = MixxxDownloadMounter(logging_adapter=logging_adapter)

        mixxx_download_remover = MixxxDownloadRemover(full_download_path,
                                                      logging_adapter)

        osx_setup_behavior = SetupBehavior('Darwin')
        osx_setup_behavior.add_setup_step(mixxx_downloader)
        osx_setup_behavior.add_setup_step(mixxx_download_mounter)
        # osx_setup_behavior.add_setup_step(mixxx_download_remover)

        platform_adapter = PlatformAdapter()
        setup_controller = SetupController(platform_adapter=platform_adapter,
                                           logging_adapter=logging_adapter)
        setup_controller.add_setup_behavior(osx_setup_behavior)

        return setup_controller


class SetupControllerModule(providers.Singleton):
    setup_controller = SetupControllerProvider()
