print('\n 1-addition', '2-substraction', '3-multiplication', '4-division', '5-Exit')
        
choice=int(input('Enter your choice'))
y=float(input('Enter first number'))
z=float(input('Enter second number'))
def add (a,b):
    ''' Function perform addition'''
    print(a+b)
if(choice==1):
    add(y,z)

def sub(c,d):
    '''Function perform substraction'''
    print(c-d)
if(choice==1):
    sub(y,z)

def mul(e,f):
    '''Function perform multiplication'''
    print(e*f)
if(choice==1):
    mul(y,z)

def div(k,l):
    '''Function perfom division'''
    print(k/l)
if(choice==1):
    div(y,z)