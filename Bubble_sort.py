#Bubble Sort
def bubble_sort(arr):
    Sorted=False
    lst_idx=len(arr)-1
    while not Sorted:
        Sorted=True
        for i in range(lst_idx):
            if arr[i]>arr[i+1]:
                Sorted=False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
print(bubble_sort([4,5,4,3,2,1]))





