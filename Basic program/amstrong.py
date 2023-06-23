lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))

print("The Armstrong numbers are:")

for num in range(lower_range, upper_range + 1):
    # Count the number of digits in the current number
    order = len(str(num))
    
    # Initialize sum variable
    sum = 0
    
    # Find the sum of the cubes of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    
    # Check if the number is an Armstrong number
    if num == sum:
        print(num)
