#write a python program to delete an element from a particular position in the tuple.
#write a python program to delete an element from a particular position in the tuple.
num = (10,20,30,40,50)

#accept position number of the wlwmwnt to delete
pos = int(input('Enter position number: '))

num1 = num[0:pos-1]

num = num1+num[pos:]
print(num)
