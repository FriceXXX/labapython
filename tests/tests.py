import pytest

from src.calc import *
from src.exception import *

@pytest.mark.parametrize('expression, result', [
    ('4 3 +', 7),
    ('5 4 *', 20),
    ('2,4 44 * (50 3 +) 11 41 + - +', 106.6)])
def test_calc(expression, result):
    assert rpn_calculator(expression) == result

@pytest.mark.parametrize('expression, exception', [
    ('4 3 + +', CalcError),
    ('5 4', CalcError),
    ('4 4 - 0 /', ZeroDivisionError),
])
def test_excep_calc(expression, exception):
    with pytest.raises(exception):
        rpn_calculator(expression)

@pytest.mark.parametrize(
    'expression, result',
    [
        ('-(2 2 +)', -4),
        ('-(2 2 +) (2 2 +) +', 0),
        ('2 (2 (2 (2 9 +) *) +) +)', 26)
    ])
def test_brackets_calc(expression, result):
    assert rpn_calculator(expression) == result

@pytest.mark.parametrize('expression, result', [
    ('(2 2 +)))', CalcError),
    ('(2 2 +) (2 2 + +) +', CalcError),
])
def test_brackets_except_calc(expression, exception):
    with pytest.raises(exception):
        rpn_calculator(expression)