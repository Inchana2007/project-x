def insertionsort(a):
    n=len(a)
    for i in range(1,n):
        k=a[j]
        j=i-1
        while j<0 and a[j]>k:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=k
            print(a)
x=[34,46,43,27,57,41]
print("before sorting:",x)
insertionsort(x)
print("after sorting:",x)
