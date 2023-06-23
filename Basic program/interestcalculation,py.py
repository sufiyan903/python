def interest_calculation(principal, years, rate):
    simple_interest = (principal * rate * years) / 100
    return simple_interest

name = input("Enter the name of the customer: ")
age = int(input("Enter the age of the customer: "))
gender = input("Enter the gender ('M' or 'F'): ")
principal_amount = float(input("Enter the principal amount: "))
number_of_years = int(input("Enter the number of years: "))

if age >= 60:
    rate_of_interest = 12
elif gender == 'F':
    rate_of_interest = 10
else:
    rate_of_interest = 9

interest = interest_calculation(principal_amount, number_of_years, rate_of_interest)

print("Customer Name:", name)
print("Principal Amount:", principal_amount)
print("Number of Years:", number_of_years)
print("Rate of Interest:", rate_of_interest, "%")
print("Simple Interest:", interest)
s
