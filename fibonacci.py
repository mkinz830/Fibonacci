# Write a Python function to print first n Fibonacci numbers

fnum = 13
n = 0
print(0)
print(1)
zero = 0
one = 1
while(n < fnum - 2):
    total = zero + one
    print(total)
    zero = one
    one = total
    n = n+1