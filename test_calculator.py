import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),  # 2 + 3 = 5
    (-5, 8, 3),  # -5 + 8 = 3
    (-90, -5, -95),  # 0 + 0 = 0
    (0.1,0.25,0.35),
     ('8', '9', 17),
])
def test_add(a, b, expected,calculator,set_function_to_add):
    result = calculator.calc(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected",[
    (2, 3, 6),  # 2 * 3 = 6
    (-5, 8, -40),  # -5 * 8 = -40
    (1.5, 2, 3),  # -5 * 8 = -40
    (0.255555555,2,0.51111111),
    (-1, -180, 180),  # 180
    (-0, 0, 0),  # 0 * 10 = 0
    
])
def test_multiply(a, b, expected,calculator,set_function_to_multiply):  
    
    result = calculator.calc(a, b)
    assert result == expected 