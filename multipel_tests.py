import pytest

@pytest.mark.one
def test_method1():
    x=3
    y=4
    assert x==y

@pytest.mark.second
def test_method2():
    a=13
    b=10
    assert a==b +3

