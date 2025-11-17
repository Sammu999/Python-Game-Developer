# Dictionary of usernames and passwords
user_credentials = {"Sammu999": "password123","Quantmedics": "Shwetamath", "Sach008": "letmein789",
                    "InvisibleTurt": "abc123","David123": "passw0rd"}

# Prompt user for input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if username exists
if username not in user_credentials:
    print("Invalid user. Access denied.")
else:
    # Check if password matches
    if user_credentials[username] == password:
        print("Login successful. Welcome to the system!")
    else:
        print("Invalid password. Please try again.")
