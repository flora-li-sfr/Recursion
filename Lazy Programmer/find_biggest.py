def find_biggest(number_list):
    length = len(number_list)

    # step 1: base case handling when N-1 becomes 1
    if length == 1:
        return number_list[0]

    # step 2: Assume N-1 has been resolved
    n_1_biggest = find_biggest(number_list[1:])

    # step 3: Handle the current element with the result of N-1
    if number_list[0] > n_1_biggest:
        return number_list[0]
    return n_1_biggest

data = [3, 5, 9, 4, 10, 2]
print("The biggest number in {} is {}".format(data, find_biggest(data)))
