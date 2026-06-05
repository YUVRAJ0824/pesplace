
# Example functions

# def greet(name):
#     print(f"Hello, {name}")
# greet("riya")

def greet(name):
    print(f"Hello {name}!")

greet("riya")


# nums = [10, 20, 30]
# for i in range(3):
#     print(nums[i])


def is_sum_above_list(num1, num2, limit=100):
    num1 = 10
    num2 = 20           
    total = num1 + num2
    # check if sum exceeds limit
    if total > limit:
        print("sum exceeds limit")
    else:
        print("sum is within limit")

is_sum_above_list(10, 20)