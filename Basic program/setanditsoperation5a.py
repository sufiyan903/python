set_a = set(input("Enter the elements of set A, separated by commas: ").split(","))
set_b = set(input("Enter the elements of set B, separated by commas: ").split(","))

is_subset = True
for element in set_b:
    if element not in set_a:
        is_subset = False
        break

print(is_subset)
