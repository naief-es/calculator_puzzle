import os
import traceback
init = False


def get_test_name():
    return os.environ.get('PYTEST_CURRENT_TEST').split('::')[1].split('[')[0]


class Calculator:
    set_function_count = 0
    test_name = ''

    def __init__(self):
        global init
        assert init is False, 'The Calculator init twice, can you use fixture with another scope?'
        init = True
        self.__func = None

    def set_function(self, func):
        assert self.set_function_count < 2, 'You got the limit of use this function,' \
                                            ' can you use fixture with another scope?'
        self.set_function_count += 1
        self.test_name = get_test_name()
        self.__func = func

    def calc(self, a, b):
        assert self.test_name == get_test_name(), "Do you use parametrize?"
        assert self.__func is not None, "no set function"
        return self.__func(a, b)


def add(a, b):
    st = traceback.extract_stack()
    assert st[len(st)-2].name == 'calc', "do you cal me via calc function?"
    return a + b


def multiply(a, b):
    st = traceback.extract_stack()
    assert st[len(st) - 2].name == 'calc', "do you cal me via calc function?"
    return a * b
