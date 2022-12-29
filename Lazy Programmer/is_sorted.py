def is_sorted(number_list):
    length = len(number_list)

    # step 1: base case handling when N-1 becomes 1
    if length == 1:
        return True
       
    # step 2: Assume N-1 has been resolved
    n_1_sorted =  is_sorted(number_list[1:])

    # step 3: Handle the current element with the result of N-1
    check = number_list[0] < number_list[1]
    return check and n_1_sorted

sorted_list = [2, 4, 6, 8, 19, 21]
not_sorted_list = [2, 4, 9, 8, 19, 11]

print("{} is sorted? {}".format(sorted_list, is_sorted(sorted_list)))
print("{} is sorted? {}".format(not_sorted_list, is_sorted(not_sorted_list)))