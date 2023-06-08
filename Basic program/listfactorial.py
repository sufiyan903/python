def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numbers = [int(x) for x in input("Enter the list of numbers: ").split()]

factorial_list = [factorial(num) for num in numbers]

print("Original list:", numbers)
print("Factorial list:", factorial_list)
