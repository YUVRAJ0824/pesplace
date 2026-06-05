arr=[10,20,30,40,50]
arr.insert(2,30)
print("after insertion:",arr)
arr.append(60)
print("after append:",arr)
arr.remove(30)
print("after remove:",arr)
popped=arr.pop()

print(f"popped: {popped}, array: {arr}")