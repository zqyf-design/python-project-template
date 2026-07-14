import pytest
from src.utils import greet, add, multiply, is_even


class TestUtils:
    def test_greet(self):
        assert greet("Alice") == "Hello, Alice!"
        assert greet("Bob") == "Hello, Bob!"
        assert greet("") == "Hello, !"

    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(100, 200) == 300

    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
        assert multiply(10, 10) == 100

    def test_is_even(self):
        assert is_even(2) == True
        assert is_even(3) == False
        assert is_even(0) == True
        assert is_even(-4) == True