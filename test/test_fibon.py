import pytest
from series.Fibonacci import  fibonacci

def test_fol_one():
    actual=fibonacci(0)
    excepted=0
    assert actual == excepted

def test_fol_two():
    actual=fibonacci(1)
    excepted=1
    assert actual == excepted

def test_fol_three():
    actual=fibonacci(2)
    excepted=1
    assert actual == excepted

def test_fol_four():
    actual=fibonacci(3)
    excepted=2
    assert actual == excepted

def test_fol_fiveSeven():
    actual=fibonacci(4)
    excepted=3
    assert actual == excepted

def test_fol_six():
    actual=fibonacci(5)
    excepted=5
    assert actual == excepted

def test_fol_fifteen():
    actual=fibonacci(6)
    excepted=8
    assert actual == excepted

def test_fol_fifteen():
    actual=fibonacci(7)
    excepted=13
    assert actual == excepted

