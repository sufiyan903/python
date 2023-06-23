def swap_strings(s1, s2):
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]
    return new_s1 + " " + new_s2

# Get user input for the two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swap the strings and get the result
result = swap_strings(string1, string2)

# Display the result
print("Swapped string:", result)
