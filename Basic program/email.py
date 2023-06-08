email = input("Enter the email id: ")

# Extracting the username
username = email.split('@')[0]

# Generating the password
password = username + username[::-1]

print("Username -", username)
print("Password -", password)
