import functools

# Parent class for all Decorator children
class Decorator(object):
	def __init__(self, func):
		self._func = func

	# Default behavior does nothing other than calling the decorated function
	def __call__(self, *args, **kwArgs):
		self._func(*args, **kwArgs)

	# Allows using this decorator with methods and functions
	def __get__(self, instance, owner):
		return functools.partial(self.__call__, instance)

# Stores computed values from decorated functions/methods and returns their values
# if they have been previously called instead of recomputing
class Memoize(Decorator):
	def __init__(self, func):
		super(Memoize, self).__init__(func)
		self.__memo = {}

	# Required to use this class as a Decorator
	def __call__(self, *args):
		# Call normal function and store its value
		if not args in self.__memo:
			self.__memo[args] = self._func(*args)

		# Return stored value
		return self.__memo[args]
