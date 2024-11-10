#quick sort
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[len(arr)//2]
    small_val=[]
    great_val=[]
    for i in arr:
        if i<pivot:
            small_val.append(i)
        elif i>pivot:
            great_val.append(i)
    return quick_sort(small_val)+[pivot]+quick_sort(great_val)
print(quick_sort([5,4,3,12,31,1]))


