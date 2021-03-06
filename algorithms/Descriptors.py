'''
Descriptor classes provide functionality for class attributes that have
shared getters and setters.  Since they are meant to be class attributes,
the parent class, Descriptor(), provides functionality that allows
class instances to have their own instance attributes through the use of
the WeakKeyDictionary.

Ex:
class MyClass(object):
    x = Descriptor()
    def __init__(self, x):
        self.x = x # Assign class attribute x with __init__ argument x
'''

from weakref import WeakKeyDictionary


class Descriptor(object):  # pylint: disable=too-few-public-methods
    ''' Parent class for all Descriptor children '''

    def __init__(self):
        self._data = WeakKeyDictionary()

    def __get__(self, instance, cls):
        return self._data[instance]

    def __set__(self, instance, value):
        self._data[instance] = value

    def __delete__(self, instance):
        del self._data[instance]


class Constant(object):  # pylint: disable=too-few-public-methods
    '''
    This descriptor class makes sure class attributes are read only
    Ex:

    class MyClass(object):
        pi = Constant(3.1415)
    '''

    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.__value)

    def __get__(self, instance, cls):
        return self.__value

    def __set__(self, instance, value):
        self.__raise_error()

    def __delete__(self, instance):
        self.__raise_error()

    @staticmethod
    def __raise_error():
        raise ValueError('Attribute is a constant.  Cannot modify.')
