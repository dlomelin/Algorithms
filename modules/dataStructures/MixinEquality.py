class MixinEquality(object):
	def __eq__(self, other):

		# Use type to make sure classes are the same as opposed to
		# isinstance() that allows flexibility.
		if type(self) is type(other):
			return self.__dict__ == other.__dict__

		return False

	def __ne__(self, other):
		return not self.__eq__(other)
