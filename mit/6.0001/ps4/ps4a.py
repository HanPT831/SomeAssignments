# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    list_of_reorder = []
    if len(sequence) <= 1:
        list_of_reorder.append(sequence)
        return list_of_reorder
    else:
        first = sequence[:1]
        remain = sequence[1:]
        # print(remain)
        reorder_of_remain = get_permutations(remain)
        # print(reorder_of_remain)
        for order in reorder_of_remain:
            for i in range(len(sequence)):
                list_of_reorder.append(order[:i] + first + order[i:])
        return list_of_reorder
   

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'aeiou'
    print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print(len(set(get_permutations(example_input))))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

