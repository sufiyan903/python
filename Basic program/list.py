def find_number_occurrence(numbers, target):
    occurrence_count = numbers.count(target)
    positive_indices = []
    negative_indices = []

    for i, num in enumerate(numbers):
        if num == target:
            positive_indices.append(i + 1)
            negative_indices.append(-(len(numbers) - i))

    print(f"Element {target} occurs {occurrence_count} times in the list.")
    print("Positive Index:", ', '.join(map(str, positive_indices)))
    print("Negative Index:", ', '.join(map(str, negative_indices)))


numbers = [2, 6, 7, 12, 17, 7, 8, 2, 6, 20, 3, 5]
target = int(input("Enter the element to be found: "))
find_number_occurrence(numbers, target)
