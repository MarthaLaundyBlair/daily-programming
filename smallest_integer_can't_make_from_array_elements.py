"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

"""

def smallest_integer(array):
    # set the first trial smallest integer to 1
    trial_smallest_integer = 1
    # loop through the array
    for i in range(len(array)):
        # if the current smallest uncheked item in the array is greater than the trial smallest integer then we have found the smallest integer
        if array[i] > trial_smallest_integer:
            smallest_integer = trial_smallest_integer
            break
        # we know that we must be able to make every integer up to the trial smallest iteger as otherwise we would have already found it
        # therefore because we only used the items up to array[i] to do this we could add array[i] to any of these
        # thus we can make any of the numbers up to the sum of the trial smallest integer and array[i]
        # therefore we must increase the trial smallest integer by array[i]
        else: 
            trial_smallest_integer = trial_smallest_integer + array[i]
    smallest_integer = trial_smallest_integer
    print ("The smallest possible integer is " + str(smallest_integer))

    return trial_smallest_integer

smallest_integer([1, 2, 3, 10])