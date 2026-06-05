#stack lifo with push pop peeek
Stack =[]
Stack.append(10)
Stack.append(20)
Stack.append(30)
print("stacks:", Stack)

print("top element:", Stack[-1])

popped=Stack.pop()
print("popped :", popped)
print("stacks after pop:", Stack)

print("isempty:", len(Stack) == 0)