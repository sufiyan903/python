a = {1, 2, 3, 4}
b = {1, 2, 3}

# Check if b is a subset of a
is_subset = True
for element in b:
    if element not in a:
        is_subset = False
        break

# Display the result
print(is_subset)
