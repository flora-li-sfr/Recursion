def str_permutation(str1):
    ret = []
    length = len(str1)

    # step 1: base case handling when N-1 becomes 
    if length == 1:
        ret.append(str1)
        return ret

    first_ch = str1[0]

    # step 2: Assume N-1 permutation is done
    rest_permutation_str = str_permutation(str1[1:])

    # step 3: Handle the first character and result of N-1 permutation by inserting 
    # it into possible position, in this example with ‘XYZ’, assuming we get N-1 
    # permutations on ‘YZ’ are ‘YZ’ and ‘ZY’, the following logic is to insert ‘X’ in ‘YZ’ and ‘ZY’
    # for ‘YZ’, it will produce ‘XYZ’, ‘YXZ’, ‘YZX’
    # for ‘ZY’, it will produce ‘XZY’, ‘ZXY’, ‘ZYZ’
    permu_length = len(rest_permutation_str)
    for i in range(0, permu_length):
        for j in range(0, len(rest_permutation_str[i])):
            ret.append(rest_permutation_str[i][0:j] + first_ch + rest_permutation_str[i][j:])
        ret.append(rest_permutation_str[i] + first_ch)
    return ret

given_str = "XYZ"
print("The permutations of {} is {}".format(given_str, str_permutation(given_str)))