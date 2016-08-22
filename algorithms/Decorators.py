'''.'''

import functools


class Decorator(object):  # pylint: disable=too-few-public-methods
    ''' Parent class for all Decorator children '''

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwArgs):
        ''' Default behavior does nothing other than calling the decorated function '''
        self._func(*args, **kwArgs)

    def __get__(self, instance, owner):
        ''' Allows using this decorator with methods and functions '''
        return functools.partial(self.__call__, instance)


class Memoize(Decorator):  # pylint: disable=too-few-public-methods
    '''
    Stores computed values from decorated functions/methods and returns their values
    if they have been previously called instead of recomputing
    '''

    def __init__(self, func):
        super(Memoize, self).__init__(func)
        self.__memo = {}

    def __call__(self, *args):
        ''' Required to use this class as a Decorator '''
        # Call normal function and store its value
        if args not in self.__memo:
            self.__memo[args] = self._func(*args)

        # Return stored value
        return self.__memo[args]
