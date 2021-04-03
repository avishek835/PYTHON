#py.test -s will print in console
#py.test test_demo2.py  -s
#py.test -k firstDemo  -s
# E:\SELENIUMPYTHON\demoPytest>py.test test_demo2.py  -s
#py.test -k -m smoke  -s
#@pytest.mark.xfail will run but not report
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstDemo():
    print("Hello Pytest")


test_firstDemo()


def test_secondDemo():
    print("Hello again Pytest")