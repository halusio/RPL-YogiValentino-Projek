# import modul yang diperlukan
import pytest
from calculator import Calculator

# mendefinisikan unit test untuk fungsi penjumlahan
def test_addition():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(0, 0) == 0
    assert Calculator.add(-5, 3) == -2
    assert Calculator.add(2.5, 4.75) == pytest.approx(7.25)

# mendefinisikan unit test untuk fungsi pengurangan
def test_subtraction():
    assert Calculator.subtract(5, 2) == 3
    assert Calculator.subtract(0, 0) == 0
    assert Calculator.subtract(-5, -3) == -2
    assert Calculator.subtract(10, 3.5) == pytest.approx(6.5)

# mendefinisikan unit test untuk fungsi perkalian
def test_multiplication():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(0, 5) == 0
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(0.5, 3) == pytest.approx(1.5)

# mendefinisikan unit test untuk fungsi pembagian
def test_division():
    assert Calculator.divide(6, 3) == 2
    assert Calculator.divide(0, 5) == 0
    assert Calculator.divide(-4, 2) == -2
    assert Calculator.divide(3.75, 1.5) == pytest.approx(2.5)
    with pytest.raises(ValueError):
        Calculator.divide(6, 0)

# menjalankan unit test
if __name__ == '__main__':
    pytest.main()
