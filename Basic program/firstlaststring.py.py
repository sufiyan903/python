def extract_string(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

# Get user input for the string
string = input("Enter a string: ")

# Extract the desired string
result = extract_string(string)

# Display the result
print("Extracted string:", result)
