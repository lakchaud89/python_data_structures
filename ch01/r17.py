def sum_odd_squares(n):
    print(sum([k*k if(k%2==1) else 0 for k in range(n)]))

sum_odd_squares(3)
sum_odd_squares(4)
