import pytest

from poetrydemo.Calculator import Calculator


@pytest.fixture(scope="module")
def calculator():
    print("Calling calculator class!!")
    return Calculator()
