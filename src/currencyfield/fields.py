from decimal import Decimal
from django.db.models import BigIntegerField
from currencyfield.utils import Currency


class CurrencyField(BigIntegerField):
	def get_prep_value(self, value):
		if isinstance(value, Currency):
			value = value.value
		elif isinstance(value, int):
			pass
		elif isinstance(value, (str, float, Decimal, )):
			value = Currency(value, external_value=True).value
		return super().get_prep_value(value)

	def from_db_value(self, value, expression, connection):
		return Currency(value)
