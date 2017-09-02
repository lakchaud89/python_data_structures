# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_odd_sqrs(n):
    i=1
    sum=0
    while(i<n):
        if(i%2 ==1):
            sum = sum + (i**2)
        i += 1
    return sum

print(sum_odd_sqrs(3))
print(sum_odd_sqrs(4))
