#write a python Program to accept elements in a form of a tuple and display there sum and average.
num=(eval(input('enter the element')))
sum=0
n=len(num)
for i in range (n):
    sum+=num[i]
    print('sum os number',sum)
    print('Average of number',sum/n)
    
