def is_armstrong(number):
    num_str = str(number)
    order = len(num_str)
    sum = 0

    for digit in num_str:
        sum += int(digit) ** order

    return sum == number

lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))

armstrong_numbers = []

for number in range(lower_range, upper_range + 1):
    if is_armstrong(number):
        armstrong_numbers.append(number)

print("The Armstrong numbers are:")
for number in armstrong_numbers:
    print(number)
