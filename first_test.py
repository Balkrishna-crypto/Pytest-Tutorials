import pytest

def fun(x):
    return x+5

def test_answer():
    assert fun(3) == 8