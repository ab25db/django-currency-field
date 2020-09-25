import pytest
from currencyfield.utils import Currency


class TestCurrencyClass:

	def test_addition(self):
		result = Currency(50.11, external_value=True) + Currency("40.50", external_value=True)
		assert isinstance(result, Currency)
		assert str(result) == "90.61"
		assert result.external_value == 90.61

		# this addition will be on the thousandth of a cent value so it wont move the needed much when casted to dollars
		result = Currency(50.11, external_value=True) + 40.50
		assert isinstance(result, Currency)
		assert str(result) == "50.11"
		assert result.external_value == 50.11

	def test_subtraction(self):
		result = Currency(50.11, external_value=True) - Currency("40.50", external_value=True)
		assert isinstance(result, Currency)
		assert str(result) == "9.61"
		assert result.external_value == 9.61

		# this math will be on the thousandth of a cent value so it wont move the needed much when casted to dollars
		result = Currency(50.11, external_value=True) - 40.50
		assert isinstance(result, Currency)
		assert str(result) == "50.11"
		assert result.external_value == 50.11

	def test_multiplication(self):
		with pytest.raises(TypeError):
			Currency(50.11, external_value=True) * Currency("3", external_value=True)

		result = Currency(50.11, external_value=True) * 5.5
		assert isinstance(result, Currency)
		assert str(result) == "275.61"
		assert result.external_value == 275.61

		result = Currency(50.11, external_value=True) * 2
		assert isinstance(result, Currency)
		assert str(result) == "100.22"
		assert result.external_value == 100.22

		val = Currency(454.23, external_value=True)
		val = val * 6
		assert val.external_value == 2725.38

	def test_division(self):
		with pytest.raises(TypeError):
			Currency(50.11, external_value=True) / Currency("3", external_value=True)

		result = Currency(50.11, external_value=True) / 5.5
		assert isinstance(result, Currency)
		assert str(result) == "9.11"
		assert result.external_value == 9.11

		result = Currency(50.11, external_value=True) / 2
		assert isinstance(result, Currency)
		assert str(result) == "25.05"
		assert result.external_value == 25.05

		val = Currency(454.23, external_value=True)
		val = val / 43.25
		assert val.external_value == 10.5

	def test_bool(self):
		total = Currency(0)
		assert not total
		assert not bool(total)

	def test_negative(self):
		refund_amount = Currency("-500.34", external_value=True)
		assert refund_amount.value < 0
		assert refund_amount.external_value < 0
		assert refund_amount.external_value == -500.34

	# def test_small(self):
	# 	val = Currency("0.0001", external_value=True)
	# 	assert val.external_value == 0.0001
	#
	# 	val = Currency("0.001", external_value=True)
	# 	assert val.external_value == 0.001
	#
	# 	val = Currency("0.01", external_value=True)
	# 	assert val.external_value == 0.01
