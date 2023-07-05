start_range = 1
end_range = 9

factors = {}

for num in range(start_range, end_range + 1):
    factors[num] = {i for i in range(1, num + 1) if num % i == 0}

print(factors)
