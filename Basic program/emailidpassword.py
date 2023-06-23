def generate_password(email):
    username = email.split("@")[0]  # Extract the username before the @ symbol
    password = username + username[::-1].upper()  # Combine username and reverse uppercase username
    return username, password

# Get user input for the email ID
email_id = input("Enter the email id: ")

# Generate the password
username, password = generate_password(email_id)

# Display the result
print("Username -", username)
print("Password -", password)
