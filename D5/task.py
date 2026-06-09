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



"""
system hosptial with highest priority are treated input
 patient a,b,c
 prioty order is a=3,b=1,c=5
using queue
# tested own method=flop faah
print("\npatient priority assigned treating")
#importing lib queue and this types
from queue import PriorityQueue

patients = PriorityQueue()
#setting order syntax name.put((order,'name'))
patients.put((-3, 'Patient A')) 
patients.put((-1, 'Patient B')) 
patients.put((-5, 'Patient C'))  

print("patients priority :")
 
"""

import heapq
patients = []
heapq.heappush(patients,(-3,"A"))
heapq.heappush(patients,(-1,"B"))

heapq.heappush(patients,(-%,"C"))
while patients:
    print(heapq.heapqpop{patients[1]})

    
    
"""
online store product with id and custmoer search by id searching Millions of products is low
 products=[1005,1001,1020,1015,1010,1025]
 target=1015
 insertion sort 
 op=produuct found at index 3
 else return 

 sort list then check id exists or not 


"""