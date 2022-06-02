def TOH(n,a,b,c):
    if n==1:
        print("Move disk 1 from rod {} to rod {}".format(a,c))
        return
    TOH(n-1,a,c,b)
    print("Move disk {} from rod {} to rod {}".format(n,a,c))
    TOH(n-1,b,a,c)

disk=3
TOH(disk,"A","B","C")