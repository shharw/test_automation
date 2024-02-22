import unittest
from eq_solver import square_eq_solver

class TestSquareEquationSolver(unittest.TestCase):
    def test_discriminant_zero(self):
        result = square_eq_solver(1, -6, 9)
        self.assertEqual(result, [3.0])

    def test_discriminant_positive(self):
        result = square_eq_solver(1, 2, -3)
        self.assertEqual(result, [1.0, -3.0])

    def test_discriminant_negative(self):
        result = square_eq_solver(4, -5, 6)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
