def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
            return-1
arr=(3,4,6,8,9,11)
target=4
result=binary_search(arr,target)
if result==-1:
    print("target value is not found in list")
    else:
        print("target value is not found in list")
        