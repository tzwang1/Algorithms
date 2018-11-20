'''
This problem was asked by Pinterest.

The sequence [0, 1, ..., N] has been jumbled, 
and the only clue you have for its order is an 
array representing whether each number is larger 
or smaller than the last. Given this information, 
reconstruct an array that is consistent with it. 
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
'''

def reconstruct_array(sequence):
    arr = [0] * len(sequence)
    cur_max = len(sequence) - 1
    cur_min = 0

    for i in range(len(arr)-1, -1, -1):
        if sequence[i] == '+':
            arr[i] = cur_max
            cur_max-=1
        else:
            arr[i] = cur_min
            cur_min+=1
    
    return arr

if __name__ == "__main__":
    sequence = [None, '+', '+', '-', '+']
    seq1 = [None]
    seq2 = []
    
    print(reconstruct_array(sequence))
    print(reconstruct_array(seq1))
    print(reconstruct_array(seq2))