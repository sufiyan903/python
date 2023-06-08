number = int(input("Enter the number: "))
power = int(input("Enter the power: "))

result = number ** power

if result % 2 == 0:
    print(f"The {power}th power of {number} is even.")
else:
    print(f"The {power}th power of {number} is not even.")
