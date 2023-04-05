import pytest
from series.Sumseries import sum_series

def test_six_s0():
    actual = sum_series(6)
    expected = 8
    assert actual == expected    

def test_six_s1():
    actual = sum_series(6,2,1)
    expected = 18
    assert actual == expected     

def test_six_s2():
    actual = sum_series(6,3,2)
    expected = 31
    assert actual == expected 