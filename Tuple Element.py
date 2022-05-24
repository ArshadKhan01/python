#write a python program to find first occurance of an element in tuple.

st =input('enter the element separated by commas:  ').split(',')
lst=[int(num) for num in st]
tup=tuple(lst)
print('the tuple is', tup)
#searching eleement
ele=int(input('enter the element to search:'))
try:
    pos=tup.index(ele)
    print('element position number:',pos+1)
except ValueError:
    print('Element not found in tuple')
