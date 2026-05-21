import re
import random

print("=" * 30)
print(" PASSWORD STRENGTH ANALYZER ")
print("=" * 30)

# Common weak passwords
common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "abc123"
]

# User input
password = input("Enter Your Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1
else:
    print(" Password should be at least 8 characters long")

# Uppercase Check
if re.search("[A-Z]", password):
    score += 1
else:
    print(" Add at least one CAPITAL letter")

# Lowercase Check
if re.search("[a-z]", password):
    score += 1
else:
    print(" Add at least one small letter")

# Number Check
if re.search("[0-9]", password):
    score += 1
else:
    print(" Add at least one number")

# Special Character Check
if re.search("[@#$%^&*!]", password):
    score += 1
else:
    print(" Add at least one special character")

# Common Password Check
if password in common_passwords:
    print(" This is a very common password")
    score = 0

percentage = (score / 5) * 100
print("Strength:", percentage, "%")

# Final Result
print("\n------ RESULT ------")

if score <= 2:
    print(" Weak Password")
elif score == 3 or score == 4:
    print(" Medium Password")
else:
    print(" Strong Password")

# Strong Password Suggestions
suggestions = [
    "loyal@2026",
    "Alpha#789",
    "Arjun$567",
    "Secure@123",
    "Python&2026"
]

print("\nSuggested Strong Password:")
print(random.choice(suggestions))