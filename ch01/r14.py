# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_squares(n):
    i = 1
    sum = 0

    while (i < n):
        sum = sum + (i ** 2)
        i += 1

    return sum



print(sum_squares(3))
print(sum_squares(4))
