def balance(n):
    # step 1: base case handling when the month is just starting
    if n == 0:
         return 100

    # step 2: get the previous month’s balance as a new base
    base = balance(n-1)

    # step 3: calculate the new balance of the current month with the formula
    return 1.01 * (base + 10) 

print("Balance after {} months is {}".format(6, balance(6)))
