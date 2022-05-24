a=[]
n=int(input("Enter a numbers of element"))
for i in range(1,n+1):
    b=int(input("Enter a numbers of element"))
    a.append(b)
a.sort()
print("Largest element:",a[n-1])