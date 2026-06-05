def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  
number=[10,11,12,13,14]
target=11

result=binary_search(number,target)
if result != -1:
    print(f"Element {target} found at index: {result}")     
else:  
    print(f"Element {target} not found in the array.")