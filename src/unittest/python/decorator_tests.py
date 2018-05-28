

import unittest


class DecoratorTest(unittest.TestCase):

    def test_pass_argument(self):

        def myDecorator():
            def decorator(f):
                def wrapper(*args, **kwargs):
                    print("Here's something")
                    f(*args, **kwargs)
                return wrapper
            return decorator

        @myDecorator()
        def myFunction(var):
            print('Hello {}', var)

        myFunction('Connor')
