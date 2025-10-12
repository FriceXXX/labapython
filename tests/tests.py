import pytest

from src.calc import *
from src.exception import *

@pytest.mark.parametrize('expression, result', [
    ('4 3 +', 7),
    ('5 4 *', 20),
    ('2.4 44 * (50 3 +) 11 41 + - +', 106.6)])
def test_calc(expression, result):
    assert solve(expression) == result

@pytest.mark.parametrize('expression, exception', [
    ('4 3 + +', CalcError),
    ('5 4', CalcError),
    ('4 5 - 0 /', CalcError),
])
def test_except_calc(expression, exception):
    with pytest.raises(exception):
        solve(expression)

@pytest.mark.parametrize(
    'expression, result',
    [
        ('-(2 2 +)', -4),
        ('-(2 2 +) (2 2 +) +', 0),
        ('2 (2 (2 (2 9 +) *) +) +', 26)
    ])
def test_brackets_calc(expression, result):
    assert solve(expression) == result

@pytest.mark.parametrize('expression, exception', [
    ('(2 2 +)))', CalcError),
    ('(2 2 +) (2 2 + +) +', CalcError)])
def test_brackets_except_calc(expression, exception):
    with pytest.raises(exception):
        solve(expression)