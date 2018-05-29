import subprocess, sys
from dmr.utils.logging.logging_adapter import ILoggingAdapter


class ProcessAdapter(object):

    def __init__(self, logging_adapter: ILoggingAdapter):
        self.logger = logging_adapter

    def run(self, *args: str):
        self.logger.info(' '.join(args), 'magenta', indentation=1)
        completed_process: subprocess.CompletedProcess = subprocess.run(args, encoding='UTF-8',
                                                                        stdout=subprocess.PIPE,
                                                                        stderr=subprocess.PIPE)
        self.logger.info(completed_process.stdout, indentation=1)
        if completed_process.stderr:
            self.logger.info(completed_process.stderr, 'red', indentation=1)
        if completed_process.returncode != 0:
            sys.exit(completed_process.returncode)
