def find_longest_asc_string(str):
    # step 1: base case handling when N-1 becomes 1 or 0
    length = len(str)
    if length == 0:
        return ""
    if length == 1:
        return str

    # additional logic to get the current ascending unit.        
    cur_len = 1
    for i in range(1, len(str)):
        if str[i] < str[i - 1]:
            break
        cur_len += 1
    cur_longest_str = str[0:cur_len]

    # step 2: Assume N-1 of longest strings have been found 
    next_longest_str = find_longest_asc_string(str[cur_len:])

    # step 3: Handle the current ascending substring with the result of N-1 ascending substring
    if len(cur_longest_str) > len(next_longest_str):
        return cur_longest_str
    else:
        return next_longest_str


given_str =  "12312345678912345612abcdefghijklmn"
print("The longest ascending substring of {} is {}".format(given_str, 
       find_longest_asc_string(given_str)))
