#dsa assigemnt d4
# 1. Second Largest Element
# 2. Remove Duplicates 
# 3. Count Occurrences
# 4. Linked List Length
# 5. Reverse Linked List
# 6. Reverse String (Stack)
# 7. Balanced Brackets
# 8. Printer Queue
# 9. Middle of Linked List
# 10. Stack using Two Queues

# Q1: Second Largest Element

def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


# 2Remove Duplicates

def remove_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result


# 3Count Occurrences

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# 4Linked List Length

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    return count

# 6Reverse String (Stack)

def reverse_string(s):
    stack = list(s)
    rev = ""
    while stack:
        rev += stack.pop()
    return rev

# 5Reverse Linked List

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

def print_linked_list(head):
    result = []
    temp = head
    while temp:
        result.append(str(temp.data))
        temp = temp.next
    return " -> ".join(result)

# 7Balanced Brackets

def balanced_brackets(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

# 9Middle of Linked List

def middle_of_linked_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# 10Stack using Two Queues

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        return self.q1.popleft() if self.q1 else None
    
    def peek(self):
        return self.q1[0] if self.q1 else None

# 8Printer Queue

from collections import deque

def printer_queue():
    queue = deque(["job1", "job2", "job3"])
    while queue:
        print("Processing:", queue.popleft())


# Main
if __name__ == "__main__":
    print("1. Second Largest Element")
    arr1 = [10, 5, 8, 15, 3, 12]
    print(f"Array: {arr1}")
    print(f"Result: {second_largest(arr1)}\n")
    
    print("2. Remove Duplicates")
    arr2 = [1, 2, 2, 3, 3, 3, 4]
    print(f"Array: {arr2}")
    print(f"Result: {remove_duplicates(arr2)}\n")
    
    print("3. Count Occurrences")
    arr3 = [1, 2, 3, 2, 2, 4, 2]
    target = 2
    print(f"Array: {arr3}, Target: {target}")
    print(f"Result: {count_occurrences(arr3, target)}\n")
    
    print("4. Linked List Length")
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    print(f"Linked List: 1 -> 2 -> 3")
    print(f"Result: {count_nodes(head)}\n")
    
    print("5. Reverse Linked List")
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3)
    print(f"Original: {print_linked_list(head2)}")
    reversed_head = reverse_linked_list(head2)
    print(f"Result: {print_linked_list(reversed_head)}\n")
    
    print("6. Reverse String (Stack)")
    s = "hello"
    print(f"Original: {s}")
    print(f"Result: {reverse_string(s)}\n")
    
    print("7. Balanced Brackets")
    brackets = ["()", "({[]})", "({[}])", "[()"]
    for b in brackets:
        print(f"'{b}': {balanced_brackets(b)}")
    print()
    
    print("8. Printer Queue")
    printer_queue()
    print()
    
    print("9. Middle of Linked List")
    head3 = Node(1)
    head3.next = Node(2)
    head3.next.next = Node(3)
    head3.next.next.next = Node(4)
    head3.next.next.next.next = Node(5)
    print(f"Linked List: 1 -> 2 -> 3 -> 4 -> 5")
    print(f"Result: {middle_of_linked_list(head3)}\n")
    
    print("10. Stack using Two Queues")
    stack = StackUsingQueues()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Pushed: 1, 2, 3")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")


