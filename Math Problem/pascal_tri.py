# a function to print each pascal triangle row
def print_pascal_row(row):
    for i in range(0, len(row)):
        print(row[i], end=" ")
    print("")

def pascal(n):
    # step 1: handle the base case, which is the first row 
    if n == 1:
        row = [1]
    else:
       # step 2: get the row value of n-1 in order to calculate pascal triangle in step 3
        prev_row = pascal(n-1)

       # step 3: using the  (r − 1,c − 1) + (r − 1,c) formula to calculate the interior values
        row = [1]
        for i in range(0, n-2):
            row.append(prev_row[i] + prev_row[i+1])
        row.append(1)

    print_pascal_row(row)
    return row

pascal(6)