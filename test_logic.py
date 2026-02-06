import pytest
from main import add, multiply, divide

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    # Ката учурун текшерүү
    with pytest.raises(ValueError):
        divide(10, 0)
