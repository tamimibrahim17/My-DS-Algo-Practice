# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.If the input array is empty or null, return an empty array:

# The passed array should NOT be changed

# input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# return [10, -65].


def count_positives_sum_negatives(arr):
    ret = []
    pos = 0
    neg = 0
    
    for i in arr:
        if i > 0:
            pos += 1
        else:
            neg += i
            
    ret.append(pos)
    ret.append(neg)
    
    if len(arr) == 0:
        return []
    
    return ret