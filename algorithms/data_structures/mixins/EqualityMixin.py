'''.'''

class EqualityMixin(object):  # pylint: disable=too-few-public-methods
    '''
    Checks if objects are of the same type and have the same attributes
    '''
    def __eq__(self, other):
        if type(self) is type(other):
            return self.__dict__ == other.__dict__

        return False

    def __ne__(self, other):
        return not self.__eq__(other)
