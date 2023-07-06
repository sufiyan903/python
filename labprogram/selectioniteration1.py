def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(n):
    num = str(n)
    reversed_num = num[::-1]
    if num == reversed_num:
        return True
    else:
        return False

# Get user input
number = int(input("Enter an integer: "))

# Check if number is odd or even
if number % 2 != 0:
    # Find factorial
    fact = factorial(number)
    print("Factorial:", fact)

    # Find number of digits in factorial
    num_digits = len(str(fact))
    print("Number of digits in factorial:", num_digits)
else:
    # Check if number is a palindrome
    if is_palindrome(number):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
