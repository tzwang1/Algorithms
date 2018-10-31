'''
Write a program that takes an array A and an index i into A,
and rearranges the elements such that all elements less than
A[i] (the "pivot") appear first ,folowed by elements equal to
the pivot, follwed by elements greater than the pivot

Ideas: 

Iterate through the array, counting the number of 
elements equal to the pivot value.

Use three pointers to keep track of where to insert
values less than the pivot, values equal to the pivot,
and values greater than the pivot


Requires 2 passes through the array.
O(n) time
O(1) space
'''

def dutch_flag_partition(pivot_idx, arr):
    pivot_val = arr[pivot_idx]
    count_equal = 0

    for i in range(len(arr)):
        if arr[i] == pivot_val:
            count_equal+=1

    less_idx = 0
    equal_idx = count_equal
    greater_idx = len(arr)-1

    while less_idx < equal_idx:
        if arr[less_idx] < pivot_val:
            less_idx+=1
            continue
        elif arr[less_idx] == pivot_val:
            arr[less_idx], arr[equal_idx] = arr[equal_idx], arr[less_idx]
            equal_idx+=1
        else:
            arr[less_idx], arr[greater_idx] = arr[greater_idx], arr[less_idx]
            greater_idx-=1
    
    return arr
