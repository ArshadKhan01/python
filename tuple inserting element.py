name = ('arshad','bilal','yogesh','sapna')

#accept the new name and position
lst = [input('enter new name: ')]
new = tuple(lst)
pos = int(input('Enter position no: '))

#copy from 0th to pos-2 into another tuple names1
name1 = name[0:pos-1]

#concatenate new element at pos-1
name1 = name1+new

#concatenate the remaining elements of names from pos-1 till end
name = name1+name[pos-1:]
print(name)
