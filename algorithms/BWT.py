'''.'''


class BWT(object):
    ''' Burrows Wheeler Transform algorithm '''

    def __init__(self, eos='$'):
        self.__eos = eos

        self.__reset_transform_data()

    ##################
    # Public Methods #
    ##################

    def transform(self, input_string):
        '''
        Creates transform data needed for backward_search method
        Populates the data structures to enable self.get_transform_string() and
        self.get_front_string()

        :param input_string:  String -

        :return:  None
        '''
        self.__reset_transform_data()

        # Make sure end of string character is not already present and then
        # append eos to string
        if self.__eos in input_string:
            raise Exception(
                'Invalid end of string character specified.  "%s" found in input.' % (self.__eos)
            )
        input_string = '%s%s' % (input_string, self.__eos)

        # Create the table necessary for the transform
        transform_table = []

        # Generate a list of cyclically shifted strings, then sort them
        for i in xrange(len(input_string)):
            cyclic_string = '%s%s' % (input_string[i:], input_string[:i])
            # Store the cyclical string and its 1 indexed original position
            transform_table.append((cyclic_string, i+1))

        transform_table = sorted(transform_table)

        # Return a string compsed of the characters from the final column
        for i in xrange(len(transform_table)):
            first_char = transform_table[i][0][0]
            last_char = transform_table[i][0][-1]
            original_index = transform_table[i][1]

            self.__char_index_obj.add(first_char, i, original_index)
            self.__occurence_table_obj.add(last_char, i)
            self.__front_column.append(first_char)
            self.__transform_column.append(last_char)

    def inverse_transform(self, input_string):
        '''
        Reverses a BWT transformed string to its initial state

        :param input_string:  String - BWT transformed string
        '''

        # Make sure end of string character is found
        if not self.__eos in input_string:
            raise Exception('End of string character "%s" not found.' % (self.__eos))

        string_len = len(input_string)

        # Create the table necessary for the inverse transform
        transform_table = [''] * string_len

        for i in xrange(string_len):

            # Add the transformed string to the prior string
            for j in xrange(string_len):
                transform_table[j] = '%s%s' % (input_string[j], transform_table[j])

            # Sort the table alphabetically
            transform_table = sorted(transform_table)

        # Iterate through the table until the string with a trailing eos character is found
        for i in xrange(string_len):
            if transform_table[i].endswith(self.__eos):
                return transform_table[i].rstrip(self.__eos)

        # Something is seriously wrong if this is called
        raise Exception('inverse_transform() could not find string with trailing eos character')

    def backward_search(self, pattern):
        '''
        Performs the backward_search algorithm which identifies where the user
        defined pattern is found in the transformed data structure.

        :param pattern:  String - Sequence pattern

        :return:  Tuple - Integers of the pattern coordinates
        '''

        pattern_index = len(pattern) - 1
        current_char = pattern[pattern_index]

        first_index = self.__char_index_obj.get_first_index(current_char)
        last_index = self.__char_index_obj.get_last_index(current_char)

        while first_index <= last_index and pattern_index >= 1 and \
            not(first_index is None or last_index is None):
            current_char = pattern[pattern_index - 1]

            first_index = self.__last_to_front(current_char, first_index - 1)
            # Handling to add 1 when return value is None
            try:
                first_index += 1
            except TypeError:
                pass
            last_index = self.__last_to_front(current_char, last_index)

            pattern_index -= 1

        # Convert index values to None when pattern was not found
        if first_index > last_index:
            (first_index, last_index) = (None, None)

        return (first_index, last_index)

    def get_original_index(self, index):
        '''
        :param index:  Integer - Position of the character

        :return:  Integer
        '''
        return self.__char_index_obj.get_original_index(index)

    def get_transform_string(self):
        '''
        :param:  None

        :return:  String
        '''
        return ''.join(self.__transform_column)

    def get_front_string(self):
        '''
        :param:  None

        :return:  String
        '''
        return ''.join(self.__front_column)

    ###################
    # Private Methods #
    ###################

    def __reset_transform_data(self):
        self.__front_column = []
        self.__transform_column = []
        self.__char_index_obj = CharacterIndex()
        self.__occurence_table_obj = OccurrenceTable()

    # Finds the index corresponding to the prior character in the original string
    def __last_to_front(self, char, index):
        try:
            return self.__char_index_obj.get_first_index(char) + \
            self.__occurence_table_obj.get_value(char, index) - 1
        except TypeError:
            return None


class CharacterIndex(object):
    ''' Needed for BWT algorithm '''

    def __init__(self):
        self.__data = {}
        self.__index_map = {}

    ########################
    # Operator Overloading #
    ########################

    def __str__(self):
        string_data = []
        for key in self.__data:
            string_data.append(
                '%s: [%s, %s]' % (
                    key,
                    self.get_first_index(key),
                    self.get_last_index(key),
                )
            )
        return '\n'.join(string_data)

    ##################
    # Public Methods #
    ##################

    def add(self, char, index, original_index):
        '''
        Adds a character and its coordinates to this instance

        :param char:  String - Single character
        :param index:  Integer - Position of the character
        :param original_index:  Integer - Position of the character in the transform table

        :return:  None
        '''
        if not char in self.__data:
            self.__data[char] = {'first': index, 'last': index}
        else:
            self.__data[char]['last'] = index

        self.__index_map[index] = original_index

    def get_original_index(self, index):
        '''
        :param index:  Integer - Position of the character

        :return:  Integer
        '''
        try:
            return self.__index_map[index]
        except KeyError:
            return None

    def get_first_index(self, char):
        '''
        :param char:  String - Single character

        :return:  Integer
        '''
        try:
            return self.__data[char]['first']
        except KeyError:
            return None

    def get_last_index(self, char):
        '''
        :param char:  String - Single character

        :return:  Integer
        '''
        try:
            return self.__data[char]['last']
        except KeyError:
            return None


class OccurrenceTable(object):
    ''' Needed for BWT algorithm '''

    def __init__(self):
        self.__data = []

    ########################
    # Operator Overloading #
    ########################

    def __iter__(self):
        for i in xrange(len(self.__data)):
            yield self.__data[i]

    def __str__(self):
        string_data = []

        for data in self:
            string_data.append(str(data))

        return '\n'.join(string_data)

    ##################
    # Public Methods #
    ##################

    def add(self, char, index):
        '''
        :param char:  String - Single character
        :param index:  Integer - Position of the character

        :return:  None
        '''
        # Copy the previous index's dictionary.
        # Should only fail when index == 0
        try:
            new_dict = self.__data[index-1].copy()
        except IndexError:
            new_dict = {char: 0}

        # Increase the counter for the current character.
        # If it's this character's first occurrence, backtrace
        # through the previous entries to fill in zero values.
        try:
            new_dict[char] += 1
        except KeyError:
            new_dict[char] = 1
            for i in xrange(index):
                self.__data[i][char] = 0

        self.__data.append(new_dict)

    def get_value(self, char, index):
        '''
        :param char:  String - Single character
        :param index:  Integer - Position of the character

        :return:  Integer
        '''
        try:
            return self.__data[index][char]
        except KeyError:
            return None
