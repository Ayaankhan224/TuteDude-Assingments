n=int(input('Enter number: '))
#
def fact(n):
    if n < 2:
        return 1
    else:
        return fact(n-1)*n
#
print(fact(n))