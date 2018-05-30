import subprocess, sys
from dmr.utils.logging.logging_adapter import ILoggingAdapter


class ProcessAdapter(object):

    def __init__(self, logging_adapter: ILoggingAdapter):
        self.logger = logging_adapter

    def run(self, depth: int, *args: str):
        self.logger.info(' '.join(args), 'magenta', indentation=depth)
        completed_process: subprocess.CompletedProcess = subprocess.run(args, encoding='UTF-8',
                                                                        stdout=subprocess.PIPE,
                                                                        stderr=subprocess.PIPE)
        self.logger.info(completed_process.stdout, indentation=depth+1)
        if completed_process.stderr:
            self.logger.info(completed_process.stderr, 'red', indentation=depth+1)
        if completed_process.returncode != 0:
            sys.exit(completed_process.returncode)
