def is_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

n = int(input("Enter number of elements in list: "))
numbers = []
for i in range(n):
    num = int(input("Enter the value: "))
    numbers.append(num)

print("Original list:", numbers)

if is_ascending(numbers):
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
