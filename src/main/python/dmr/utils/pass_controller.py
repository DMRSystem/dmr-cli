
from dependency_injector.providers import Provider
from functools import update_wrapper


def pass_controller(injector: Provider):
    def decorator(f):
        def wrapper(*args, **kwargs):
            return f(injector(), *args, **kwargs)
        return update_wrapper(wrapper, f)
    return decorator
