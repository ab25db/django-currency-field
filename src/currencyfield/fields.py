from decimal import Decimal
from django.db.models import BigIntegerField
from rest_framework.serializers import IntegerField
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


class CurrencySerializerField(IntegerField):

	def to_representation(self, obj):
		return obj.external_value if isinstance(obj, Currency) else obj

	def to_internal_value(self, data):
		if isinstance(data, Currency):
			data = data.value
		elif isinstance(data, (int, str, float, Decimal)):
			data = Currency(data, external_value=True).value
		return super().to_internal_value(data)
