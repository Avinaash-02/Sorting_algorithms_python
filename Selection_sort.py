#Selection Sort:
def selection_sort(arr):
    l=len(arr)
    index_range=range(0,len(arr)-1)
    for i in index_range:
        min_val=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_val]:
                min_val=j
        if min_val!=i:
            arr[min_val],arr[i]=arr[i],arr[min_val]
    return arr
print(selection_sort([8,6,5,4,31,2,1,10,0]))
