# ==========================================
# PYTHON LOOPS ASSIGNMENT SOLUTIONS
# ==========================================

# --- Q.1: Print numbers from 1 to 10 using a for loop ---
print("--- Q.1: Numbers from 1 to 10 ---")
for i in range(1, 11):
    print(i, end=" ")
print("\n")


# --- Q.2: Print all even numbers from 1 to 20 using a loop ---
print("--- Q.2: Even Numbers from 1 to 20 ---")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")


# --- Q.3: Print the multiplication table of 5 from 5 x 1 to 5 x 10 ---
print("--- Q.3: Multiplication Table of 5 ---")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print()


# --- Q.4: Calculate the sum of numbers from 1 to 10 using a loop ---
print("--- Q.4: Sum of Numbers from 1 to 10 ---")
total_sum = 0
for i in range(1, 11):
    total_sum += i
print(f"The sum of numbers from 1 to 10 is: {total_sum}\n")


# --- Q.5: Print numbers from 10 to 1 in reverse order using a loop ---
print("--- Q.5: Numbers from 10 to 1 in Reverse ---")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")