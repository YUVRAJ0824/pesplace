#id=[101,205,310,415,520] emp id chekc by HR 
#target=310
# using linear search
print("linear")
def linears(id, target):
    for i in range(len(id)):
        if id[i] == target:
            return i   
    return -1  
"""
testing case should print in {}

"""
id = [101, 205, 310, 415, 520]
target = 310
result = linears(id, target)

if (result != -1):
    print(f"found at index: {result}")
else:
    print("not found")

#books are arrnaged in ascending order of ISBN numbers 
#find whether an isbn exists or not
print("\nbinary")

def binary(arr, target):
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

ISBN=[10,11,12,13,14]
target=11

result=binary(ISBN,target)
if result != -1:
    print(f"Element {target} found at index: {result}")     
else:  
    print(f"Element {target} not found in the array.")


    #return -1 and index value only if found


print("\nparking vehicleslot using linear search")
#shopping mall vehicle parking lot has x vehcile naumber and check if determin is parked or not 
#show which index/slot at parked if not return -1 if found reutn inedex only no text
def parking(vehicle, target):
    for i in range(len(vehicle)):
        if vehicle[i] == target:
            return i    
    return -1

vehicle = ["ka01ab1234","ka05xy7890","ka03mn4567","ka09pq111"]
target = "ka03mn4567"

result = parking(vehicle, target)
print("vehicle found at slot:", result)
# {} or , method use this
print(f"vehicle found at slot: {result}")
