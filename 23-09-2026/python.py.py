# ==========================================
# NESTED IF-ELSE ASSIGNMENT SOLUTIONS
# ==========================================

print("------------------------------------------")
print("        ASSIGNMENT PROGRAMS STARTED       ")
print("------------------------------------------\n")


# ==========================================
# Q.1: Take number from user and check if number is greater than 50 then check number is even or not
# ==========================================
print("--- Q.1: Number > 50 & Even/Odd Checker ---")
num1 = int(input("Enter a number: "))

if num1 > 50:
    print(f"Yes, {num1} is greater than 50.")
    if num1 % 2 == 0:
        print(f"And {num1} is an Even number.\n")
    else:
        print(f"And {num1} is an Odd number.\n")
else:
    print(f"No, {num1} is not greater than 50.\n")


# ==========================================
# Q.2: Student Grade
# Take marks as input.
# If marks are 40 or above, check whether the student scored 75 or above.
# Print "Distinction" or "Pass". Otherwise, print "Fail".
# ==========================================
print("--- Q.2: Student Grade System ---")
marks = float(input("Enter student marks: "))

if marks >= 40:
    if marks >= 75:
        print("Result: Distinction\n")
    else:
        print("Result: Pass\n")
else:
    print("Result: Fail\n")


# ==========================================
# Q.3: Number Checking
# Take a number from the user.
# If the number is positive, check whether it is even or odd.
# If it is not positive, print "Negative or Zero".
# ==========================================
print("--- Q.3: Positive Number & Even/Odd Checking ---")
num3 = float(input("Enter a number: "))

if num3 > 0:
    print("The number is Positive.")
    if int(num3) % 2 == 0:
        print(f"And {int(num3)} is Even.\n")
    else:
        print(f"And {int(num3)} is Odd.\n")
else:
    print("Negative or Zero\n")


# ==========================================
# Q.4: Login System
# Ask the user to enter a username.
# If the username is correct, ask for the password.
# If the password is correct, print "Login Successful".
# Otherwise, print "Incorrect Password".
# ==========================================
print("--- Q.4: Login System ---")
correct_username = "admin"
correct_password = "123"

username = input("Enter username: ")
if username == correct_username:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login Successful ✅\n")
    else:
        print("Incorrect Password ❌\n")
else:
    print("Incorrect Username ❌\n")


# ==========================================
# Q.5: Eligibility for Driving License
# Take the user's age.
# If age is 18 or above, check whether the person has a valid ID.
# If both conditions are satisfied, print "Eligible".
# Otherwise, print the appropriate message.
# ==========================================
print("--- Q.5: Driving License Eligibility ---")
age = int(input("Enter your age: "))

if age >= 18:
    has_id = input("Do you have a valid ID? (yes/no): ").strip().lower()
    if has_id == "yes":
        print("Eligible for Driving License! 🚗\n")
    else:
        print("Not eligible: Valid ID is required.\n")
else:
    print("Not eligible: Age must be 18 or above.\n")


# ==========================================
# Q.6: Largest of Three Numbers
# Take three numbers as input.
# Using nested if, determine and print the largest number.
# ==========================================
print("--- Q.6: Largest of Three Numbers ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        print(f"The largest number is: {a}\n")
    else:
        print(f"The largest number is: {c}\n")
else:
    if b >= c:
        print(f"The largest number is: {b}\n")
    else:
        print(f"The largest number is: {c}\n")

print("------------------------------------------")
print("      ALL PROGRAMS COMPLETED SUCCESSFULLY!   ")
print("------------------------------------------")