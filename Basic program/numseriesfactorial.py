def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_series_sum_1(n):
    series_sum = 0.0
    for i in range(1, n + 1):
        term = i / factorial(i)
        series_sum += term
    return series_sum

def calculate_series_sum_2(n, x):
    series_sum = 0
    denominator = 2
    for i in range(1, n + 1):
        term = x / denominator
        series_sum += term
        denominator *= 2
    return series_sum

def calculate_series_sum_3(n):
    series_sum = 0
    increment = 15
    for i in range(1, n + 1):
        term = increment * i
        series_sum += term
    return series_sum

# Get user input for the type of series and the value of n (common for all series)
series_type = int(input("Choose the series type (1, 2, 3): "))
n = int(input("N: "))

# Calculate and display the result based on the chosen series type
if series_type == 1:
    result = calculate_series_sum_1(n)
    print("Series Sum:", result)
elif series_type == 2:
    x = int(input("X: "))
    result = calculate_series_sum_2(n, x)
    print("Series Sum:", result)
elif series_type == 3:
    result = calculate_series_sum_3(n)
    print("Series Sum:", result)
else:
    print("Invalid series type chosen!")
