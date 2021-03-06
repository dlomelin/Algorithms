'''.'''

import random


def randomize(array):
    '''
    This method generates N! possibilities, meaning each permutation has a
    1/N! chance of being generated.  Alternate methods do not create even
    distributions.

    1) Picking 2 random positions (randint(0, array_len-1)) yield N^N possible
       permutations, ie, k*N! == N^N only for k = 2 and n = 2.
       Any other values yield non even distributions.
    2) Randomly assigning numbers to each N positions and then sorting
       them can also yield biased results when positions get assigned the
       same random number

    :return array:  List

    :return:  None
    '''
    array_len = len(array)

    # Iterate through each position except the last one (no point in
    # swapping the final position with itself)
    for i in xrange(array_len-1):

        # Pick a random spot further down the list and swap them
        j = random.randint(i, array_len-1)
        array[i], array[j] = array[j], array[i]
