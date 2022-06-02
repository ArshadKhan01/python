def factorial(n):
    """To find factorial value"""
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
   
for i in range(1,11):
    print('Factorial of {} is {}'.format(i, factorial(i)))