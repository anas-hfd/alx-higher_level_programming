#!/user/bin/python3
"""
find the peak of an unsorted list of integers
by using the binary searsh-like algorithm
"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    '''Define the start and end indices for the search'''
    start, end = 0, len(list_of_integers) - 1

    '''Perform binary search-like comparison'''
    while start < end:
        '''calculate the middle index'''
        mid = (start + end) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
            '''Move the search range to the right'''
        else:
            end = mid
            '''Move the search range to the left'''

    '''The peak element is at 'start' or 'end' (they are equal)'''
    return list_of_integers[start]
