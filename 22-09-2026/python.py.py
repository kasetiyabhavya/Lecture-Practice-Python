# ==========================================
# ALL-IN-ONE PYTHON ASSIGNMENT PROGRAM
# ==========================================

print("=== TASK 1: Even or Odd Checker ===")
num1 = int(input("Enter a number to check even/odd: "))
if num1 % 2 == 0:
    print(f"{num1} is Even.\n")
else:
    print(f"{num1} is Odd.\n")


print("=== TASK 2: Check Greater than 100 ===")
num2 = float(input("Enter a number to check if it's greater than 100: "))
if num2 > 100:
    print(f"Yes, {num2} is greater than 100.\n")
else:
    print(f"No, {num2} is not greater than 100.\n")


print("=== TASK 3: Prime Number Check (for 17) ===")
num3 = 17
is_prime = True
for i in range(2, int(num3**0.5) + 1):
    if num3 % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"The number {num3} is a Prime number.\n")
else:
    print(f"The number {num3} is NOT a Prime number.\n")


print("=== TASK 4: Student Marks & Grades System ===")
marks = float(input("Enter student marks (0-100): "))
if 90 <= marks <= 100:
    print("Grade: A\n")
elif 80 <= marks < 90:
    print("Grade: B\n")
elif 70 <= marks < 80:
    print("Grade: C\n")
elif 60 <= marks < 70:
    print("Grade: D\n")
elif 50 <= marks < 60:
    print("Grade: E\n")
elif 0 <= marks < 50:
    print("Result: Fail (Below 50)\n")
else:
    print("Invalid marks entered!\n")


print("=== TASK 5: Check Element in List ===")
my_list = ["Ramesh", "Subhash", 12, 34, 45, 89]
print(f"Given List: {my_list}")
search_item = input("Enter an element to search in the list: ")

# Agar user number enter kare toh use integer me convert karein taaki list se match ho sake
if search_item.isdigit():
    search_item = int(search_item)

if search_item in my_list:
    print(f"'{search_item}' is PRESENT in the list! ✅")
else:
    print(f"'{search_item}' is NOT present in the list! ❌")

print("\n==========================================")
print("All tasks completed successfully!")