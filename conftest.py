import pytest
from calculator import Calculator,add,multiply
"""module , function ,session, class"""
@pytest.fixture(scope='session')
def calculator():
    """inctance from calc"""
    return Calculator()

@pytest.fixture(scope='session')
def set_function_to_add(calculator):
    calculator.set_function(add)

@pytest.fixture(scope='session')
def set_function_to_multiply(calculator):
    calculator.set_function(multiply)
