t= input("Enter a temprature")
sign=t [-1]
t=int(t[:-1])
if sign=="C" or sign == "c":
    t= round(t* (9/5)+32)
    print(str(t)+ 'F')
elif sign=="F" or sign== 'f':
    t=round((t-32)*(5/9))
    print(str(t)+ 'C')