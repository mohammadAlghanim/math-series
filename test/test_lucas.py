import pytest
from series.Lucas import lucas

def test_one():
    actual=lucas(0)
    excepted=2
    assert actual== excepted

def test_two():
    actual=lucas(1)
    excepted=1
    assert actual== excepted

def test_three():
    actual=lucas(2)
    excepted=3
    assert actual== excepted 

def test_four():
    actual=lucas(3)
    excepted=4
    assert actual== excepted

def test_five():
    actual=lucas(4)
    excepted=7
    assert actual== excepted

def test_six():
    actual=lucas(5)
    excepted=11
    assert actual== excepted

def test_Seven():
    actual=lucas(6)
    excepted=18
    assert actual== excepted