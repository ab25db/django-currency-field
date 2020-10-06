from decimal import Decimal
from django.db.models import BigIntegerField
from rest_framework.serializers import DecimalField
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
		return Currency(value) if value is not None else value


class CurrencySerializerField(DecimalField):

	def __init__(self, max_digits=20, decimal_places=6, **kwargs):
		super().__init__(max_digits, decimal_places, **kwargs)

	def to_representation(self, obj):
		return obj.external_value if isinstance(obj, Currency) else obj

	def to_internal_value(self, data):
		# run this method to validate the data input for decimal but discard its return val
		super().to_internal_value(data)
		if isinstance(data, Currency):
			pass
		elif isinstance(data, (int, str, float, Decimal)):
			data = Currency(data, external_value=True)
		else:
			raise ValueError(f'Invalid data type {type(data)} for CurrencySerializerField')
		return data
