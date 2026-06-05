def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target  
    return -1  # Return -1 if target is not found   

arr=[100,25,37,42,58]
print(linear_search(arr, 37)) 


#binary
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  