# Q.1: Create a list of numbers from 1 to 10 using list comprehension.
numbers = [i for i in range(1, 11)]
print(numbers)

print()

# Q.2: Create a list containing the squares of numbers from 1 to 10.
squares = [i**2 for i in range(1, 11)]
print(squares)

print()

# Q.3: From numbers 1 to 20, create a list containing only even numbers using list comprehension with a condition.
even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(even_numbers)

print()

# Q.4: Given the list below, create a new list containing all words in uppercase.
words = ["python", "sql", "excel", "power bi"]
upper_words = [word.upper() for word in words]
print(upper_words)

print()

# Q.5: Given the list below, create a new list containing only positive numbers using list comprehension.
numbers_list = [-5, 10, -2, 7, 0, 15, -8, 3]
positive_numbers = [num for num in numbers_list if num > 0]
print(positive_numbers)