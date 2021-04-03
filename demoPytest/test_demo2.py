import pytest


@pytest.mark.xfail
def test_firstDemo():
    print("Hello Avishek")
    a = 2
    b = 5
    assert a + 3 == 5, "Assertion is matching"


def test_secondDemo():
    print("Hello Chakraborty")
    str1 = "Hello Selenium"
    assert str1 == "Hello ", "Assertion Not matching";

@pytest.fixture()
def setup():
    print("I will execute first")

def test_fixtureDemo():
    print("I will execute steps in fixtureDemo method")
