
class ILoggingAdapter(object):

    def info(self, message, color: str = None, indentation: int = 0):
        raise NotImplementedError()
