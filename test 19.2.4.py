import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 2, 7) == 9

    def test_division_success(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 26, 8) == 18

    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 7) == 35

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')