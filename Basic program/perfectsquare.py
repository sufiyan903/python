number = int(input("Enter a number: "))

is_perfect_square = number ** 0.5 == int(number ** 0.5)

if is_perfect_square:
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
