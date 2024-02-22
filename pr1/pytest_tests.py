import pytest
from eq_solver import square_eq_solver

def inc(x):
    return x + 1

class TestClassDemoInstance():
    def test_discriminant_zero(self):
        result = square_eq_solver(1, -6, 9)
        assert result == [3.0]

    def test_discriminant_positive(self):
        result = square_eq_solver(1, 2, -3)
        assert result == [1.0, -3.0]

    def test_discriminant_negative(self):
        result = square_eq_solver(4, -5, 6)
        assert result == []
