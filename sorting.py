def quicksort(arr):
    if len(arr) <=1:
        return arr
    
    pivote = arr[len(arr)//2]
    
    left = [x for x in arr if x< pivote]
    middle = [x for x in arr if x== pivote]
    right = [x for x in arr if x> pivote]
    
    return quicksort(left) + middle +quicksort(right)


arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swapped = False
        
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped =True
        
        if swapped !=True:
            break
        
arr = [64, 34, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)       


def merge_sort(arr):
    if len(arr) <=1:
        return arr 
    
    mid = len(arr)//2
    
    left_part = merge_sort(arr[:mid])
    right_part = merge_sort(arr[mid:])
    
    return merge(left_part, right_part)

def merge(left, right):
    sortedarr = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedarr.append(left[i])
            i +=1
        else:
            sortedarr.append(right[j])
            j+=1
    
    sortedarr.extend(left[i:])
    sortedarr.extend(right[j:])
    
    return sortedarr
    

a=[45,23,12,56,78,98]
b=merge_sort(a)                
print("merge sort", b)                    