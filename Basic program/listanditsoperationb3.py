n = int(input("Enter the number of elements in the list: "))
numbers = []

# Read the list of numbers
for i in range(n):
    num = int(input(f"Enter the value - {i+1}: "))
    numbers.append(num)

# Check if the list is in ascending order
is_ascending = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

# Display the result
print("Original list:", numbers)
if is_ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
