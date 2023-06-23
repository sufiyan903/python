def calculate_power(base, power):
    result = base ** power
    return result

# Get user input for base and power
base = float(input("Base: "))
power = int(input("Power: "))

# Calculate the power of numbers
result = calculate_power(base, power)

# Display the result
print("Result:", result)
