import pytest



@pytest.fixture
## Whenever we need to run some code before test we use fixture.

def nums():
    a=5
    b=7
    c=10
    return[a,b,c]

def test_method1(nums):
    x=5
    assert nums[0]==x

def test_method2(nums):
    x=8
    assert nums[2]==x

def test_method3(nums):
    x=7
    assert nums[1]==x

