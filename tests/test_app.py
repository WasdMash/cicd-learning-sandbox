import pytest
from src.app import add_numbers, calculate_discount

def test_add_numbers():
	assert add_numbers(2, 3) == 5
	assert add_numbers(-1, 1) == 0
	assert add_numbers(0.5, 0.5) == 1.0

def test_calculate_discount():
	assert calculate_discount(100.0, 20.0) == 80.0
	assert calculate_discount(50.0, 0.0) == 50.0

def test_invalid_discount():
	with pytest.raises(ValueError):
		calculate_discount(100.0, 150.0)