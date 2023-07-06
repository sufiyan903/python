numbers = input("Enter a list of numbers, separated by commas: ").split(",")
numbers = [int(num) for num in numbers]

element = int(input("Enter the element to be found: "))

positive_indices = []
negative_indices = []

# Find the occurrence of the element and store its indices
for i in range(len(numbers)):
    if numbers[i] == element:
        positive_indices.append(i + 1)
        negative_indices.append(-(len(numbers) - i))

occurrences = len(positive_indices)

# Display the occurrence and indices
print(f"Element {element} occurs {occurrences} time(s) in the list.")
print("Positive Index:", ", ".join(map(str, positive_indices)))
print("Negative Index:", ", ".join(map(str, negative_indices)))
