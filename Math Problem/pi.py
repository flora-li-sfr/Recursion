def calculate_pi(precision):
    # step 1: base case handling when N-1 becomes 0
    if precision == 0:
        return 3

    # step 2: calculate the fraction of the current precision
    start_value = 2 * precision
    sign = 1 if precision % 2 == 1 else -1
    denominator = sign * start_value * (start_value + 1) * (start_value + 2)
    current_fraction = 4.0 / denominator

    # step 3: return the sum of the result of the PI value of the previous precision 
    #             and the fraction of the current precision
    return calculate_pi(precision -1) + current_fraction

print("PI value of the precision {} is {}".format(100, calculate_pi(100)))
