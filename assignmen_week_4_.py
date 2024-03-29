# -*- coding: utf-8 -*-
"""ASSIGNMEN_WEEK_4_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1stquNQkE8MAYzONwKGacAqc4qmrEMztg

#DATA STRUCTURE AND CONDITIONAL STATEMENT
"""

# Lists
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Sets
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", my_dict)

# Example of a conditional statement
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example 1: Check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example 2: Find the maximum of three numbers
def find_maximum(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

# Example 3: Check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the examples
def test_examples():
    # Example of a conditional statement
    check_even_odd(5)  # Output: 5 is odd.
    check_even_odd(8)  # Output: 8 is even.

    # Example 1: Check if a year is a leap year
    year = 2024
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

    # Example 2: Find the maximum of three numbers
    num1 = 10
    num2 = 25
    num3 = 15
    print("Maximum number is:", find_maximum(num1, num2, num3))

    # Example 3: Check if a number is prime
    number = 23
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Run the test
test_examples()

"""**ASSIGNMENT**"""

#Utilizing Data Structures, Conditional Statements, and Functions to solve a data-related task.

def calculate_statistics(grades):
    # Calculate average grade
    total = sum(grades)
    average = total / len(grades)

    # Find highest and lowest grade
    highest_grade = max(grades)
    lowest_grade = min(grades)

    # Count number of passing grades (assuming passing grade is 60)
    num_passing = sum(1 for grade in grades if grade >= 60)

    return average, highest_grade, lowest_grade, num_passing

def main():
    # Sample list of student grades
    student_grades = [85, 72, 60, 93, 45, 70, 88, 55, 95, 68]

    # Calculate statistics
    average_grade, highest_grade, lowest_grade, num_passing = calculate_statistics(student_grades)

    # Display results
    print("Average grade:", average_grade)
    print("Highest grade:", highest_grade)
    print("Lowest grade:", lowest_grade)
    print("Number of passing grades:", num_passing)

if __name__ == "__main__":
    main()