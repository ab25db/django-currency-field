from decimal import Decimal


class Currency:
	internal_value_multiples = {
		"USD": 100000
	}

	@property
	def external_value(self):
		val = self.value / self.internal_value_multiple
		# if we have a low value float is most likely a price point so we have to override the decimal_places to show
		if 0 < val < 0.0001 and self.decimal_places < 5:
			val = round(val, 5)
		elif 0 < val < 0.001 and self.decimal_places < 4:
			val = round(val, 4)
		elif 0 < val < 0.01 and self.decimal_places < 3:
			val = round(val, 3)
		else:
			val = round(val, self.decimal_places)
		return val

	@property
	def external_value_unrounded(self):
		val = self.value / self.internal_value_multiple
		return val

	@property
	def external_value_decimal(self):
		val = str(self.value / self.internal_value_multiple)
		return Decimal(val)

	def __init__(self, value, external_value=False, currency='USD', decimal_places=4):
		if currency not in self.internal_value_multiples:
			raise ValueError('currency does not have a internal value multiple setup')
		assert isinstance(decimal_places, int)
		self.currency = currency
		self.decimal_places = decimal_places
		if external_value is True:
			self.value = self._to_internal_value(value)
		else:
			# if not isinstance(value, int):
			# 	raise ValueError('if you are passing in a str or decimal value set external_value=True')
			self.value = int(value)

	def set_decimal_places(self, decimal_places):
		assert isinstance(decimal_places, int)
		self.decimal_places = decimal_places

	@property
	def internal_value_multiple(self):
		return self.internal_value_multiples[self.currency]

	def _to_internal_value(self, value):
		if isinstance(value, str):
			value = Decimal(value)
		return int(value * self.internal_value_multiple)

	def _clone(self, new_value):
		return Currency(new_value, currency=self.currency)

	def _prep_other_value(self, other):
		# prepares other value for math operations
		if isinstance(other, Currency):
			return other.value
		elif isinstance(other, int):
			return other
		elif isinstance(other, (str, float, )):
			return Decimal(str(other))
		elif isinstance(other, Decimal):
			pass
		return other

	def __add__(self, other):
		val = self.value + self._prep_other_value(other)
		return self._clone(val)

	def __sub__(self, other):
		val = self.value - self._prep_other_value(other)
		return self._clone(val)

	def __mul__(self, other):
		val = self.value * other
		return self._clone(val)

	def __truediv__(self, other):
		val = self.value / other
		return self._clone(val)

	def __floordiv__(self, other):
		val = self.value // other
		return self._clone(val)

	def __mod__(self, other):
		val = self.value % other
		return self._clone(val)

	def __pow__(self, other):
		val = self.value ** other
		return self._clone(val)

	def __iadd__(self, other):
		val = self.value + self._prep_other_value(other)
		return self._clone(val)

	def __isub__(self, other):
		val = self.value - self._prep_other_value(other)
		return self._clone(val)

	def __imul__(self, other):
		val = self.value * other
		return self._clone(val)

	def __idiv__(self, other):
		val = self.value / other
		return self._clone(val)

	def __ifloordiv__(self, other):
		val = self.value // other
		return self._clone(val)

	def __imod__(self, other):
		val = self.value % other
		return self._clone(val)

	def __lt__(self, other):
		return self.value < self._prep_other_value(other)

	def __le__(self, other):
		return self.value <= self._prep_other_value(other)

	def __gt__(self, other):
		return self.value > self._prep_other_value(other)

	def __ge__(self, other):
		return self.value >= self._prep_other_value(other)

	def __eq__(self, other):
		return self.value == self._prep_other_value(other)

	def __ne__(self, other):
		return self.value != self._prep_other_value(other)

	def __int__(self):
		raise self.value

	def __str__(self):
		return str(self.external_value)

	def __len__(self):
		return len(str(self.external_value))

	def __repr__(self):
		return str(self.external_value)

	def __bool__(self):
		return self.value != 0


a = Currency(1300)
