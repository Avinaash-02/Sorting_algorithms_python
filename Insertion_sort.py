#Insertion Sort
def insertion_sort(arr):
    index_range=(1,len(arr)-1)
    for i in index_range:
        value_sort=arr[i]
        while arr[i-1]>value_sort and i>0:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i-=1
    return arr
print(insertion_sort([76,55,4]))
