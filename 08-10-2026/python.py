# ==========================================
# LIST - ALL SOLUTIONS
# ==========================================


# Q.1 - Create a list of five fruits
print("--- Q.1 ---")

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Fruits:", fruits)

print()


# Q.2 - First element, last element and length
print("--- Q.2 ---")

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Length of list:", len(numbers))

print()


# Q.3 - Add 60 to the end of the list
print("--- Q.3 ---")

numbers = [10, 20, 30, 40, 50]

numbers.append(60)

print("Updated list:", numbers)

print()


# Q.4 - Insert yellow at the second position
print("--- Q.4 ---")

colors = ["red", "blue", "green"]

colors.insert(1, "yellow")

print("Updated list:", colors)

print()


# Q.5 - Remove 56 from the list
print("--- Q.5 ---")

marks = [45, 78, 56, 90, 66]

marks.remove(56)

print("Updated list:", marks)


print()

# ==========================================
# TUPLE - ALL SOLUTIONS
# ==========================================


# Q.6 - Create a tuple of five days
print("--- Q.6 ---")

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print("Days:", days)

print()


# Q.7 - Print first and last elements
print("--- Q.7 ---")

numbers = (10, 20, 30, 40, 50)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

print()


# Q.8 - Find length of the tuple
print("--- Q.8 ---")

data = ("Python", "Java", "C++", "SQL")

print("Length of tuple:", len(data))

print()


# Q.9 - Count how many times 'blue' occurs
print("--- Q.9 ---")

colors = ("red", "blue", "green", "blue")

print("Number of times 'blue' occurs:", colors.count("blue"))

print()


# Q.10 - Check whether 30 exists in the tuple
print("--- Q.10 ---")

numbers = (10, 20, 30, 40, 50)

if 30 in numbers:
    print("30 exists in the tuple.")
else:
    print("30 does not exist in the tuple.")


print()

# ==========================================
# SET - ALL SOLUTIONS
# ==========================================


# Q.11 - Create a set of five fruits
print("--- Q.11 ---")

fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

print("Fruits:", fruits)

print()


# Q.12 - Add 40 to the set
print("--- Q.12 ---")

numbers = {10, 20, 30}

numbers.add(40)

print("Updated set:", numbers)

print()


# Q.13 - Remove 20 from the set
print("--- Q.13 ---")

numbers = {10, 20, 30, 40}

numbers.remove(20)

print("Updated set:", numbers)

print()


# Q.14 - Find union of two sets
print("--- Q.14 ---")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A.union(B)

print("Union:", union)

print()


# Q.15 - Find intersection of two sets
print("--- Q.15 ---")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

intersection = A.intersection(B)

print("Intersection:", intersection)


print()

# ==========================================
# DICTIONARY - ALL SOLUTIONS
# ==========================================


# Q.16 - Create a student dictionary
print("--- Q.16 ---")

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("Student:", student)

print()


# Q.17 - Print the value of the 'name' key
print("--- Q.17 ---")

student = {
    "name": "Rahul",
    "age": 20
}

print("Name:", student["name"])

print()


# Q.18 - Add a new 'city' key
print("--- Q.18 ---")

student = {
    "name": "Rahul",
    "age": 20
}

student["city"] = "Delhi"

print("Updated dictionary:", student)

print()


# Q.19 - Change age to 21
print("--- Q.19 ---")

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi"
}

student["age"] = 21

print("Updated dictionary:", student)

print()


# Q.20 - Remove the 'city' key
print("--- Q.20 ---")

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi"
}

del student["city"]

print("Updated dictionary:", student)


print()
print("==========================================")
print("       ALL QUESTIONS COMPLETED")
print("==========================================")