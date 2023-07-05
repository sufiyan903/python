def can_obtain_from_first_string(first_string, second_string):
    # Create a set of characters from the first string
    first_set = set(first_string)

    # Check if all characters in the second string are in the first set
    for char in second_string:
        if char not in first_set:
            return "NO"

    return "YES"

# Example usage
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

result = can_obtain_from_first_string(first_string, second_string)
print(result)
