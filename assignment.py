
# Q1: Write a program that takes two numbers as input and prints their sum.
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
sum=num1+num2
print("the sum of two given number is :",sum)

# Q2:Write a python program that checks whether a given number is even or odd.
num=int(input("Enter a number: "))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")

# Q3:Write a python program that calculates the factorial of a given number
n=int(input("Enter a number: "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print("the factorial of given number is :",fac)

# Q4:Write a program that asks the user for their name and then prints a greeting message.
a=input("Enter your name :")
print("Hello",a,"welcome to the club!")

# Q5:Write a program that takes a string input from the user and writes it to a text file.
s =input("Enter the message:")
file=open(r"C:\Users\hp\OneDrive\Desktop\internship 2024\Demo1.txt",'w')
print(s,sep="!",end="##",file=file)
file.close()

# Q6:Write a program that reads the content of a text file and prints it to the console.
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")

# Example usage:
file_path = input("Enter the path of the text file: ")
read_and_print_file(file_path)

# Q7:Write a python program that takes a string as input and returns its length.
s1 = input("Enter a string: ")
print("The Length of the string is ",len(s1))

# Q8:Write a python program that concatenates two strings and returns the  result.
s2=input("Enter a string: ")
s3=input("Enter a string: ")
print("The concatenated strings are ",s2+s3)

# Q9:Write a python program that checks if a substring is present in a given  string.
s4= "Good morning Ladies and gentlemen,we gladly welcome you to our club. "
s5= input("Enter a string: ")
print(s5 in s4)

# Q10: Write a python program that converts a given string to uppercase
s6 = "python assignment"
print(s6.upper())

# Q11: Write a python program that generates the first n numbers in the Fibonacci sequence.
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_numbers = generate_fibonacci(n)
print("The first", n, "numbers in the Fibonacci sequence are:", fibonacci_numbers)




# Q12:Write a python program that calculates the sum of the digits of a given number.
n=int(input("Enter the number:"))
sum=0
for i in str(n):
    sum=sum+int(i)
print(sum)

# Q13:Write a program that asks the user for their birth year and calculates their  age
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("Your age is:", age)

# Q14:Write a program that reads multiple lines of input from the user until they  enter an empty line, then prints all the lines.
lines = []

print("Enter multiple lines of input. Enter an empty line to stop:")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\nYou entered the following lines:")
for line in lines:
    print(line)

# Q15: Write a program that reads data from a CSV file and prints it to the console.
import csv

def read_csv_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))
file_path = "C:/Users/hp/Downloads/organizations-100.csv"
read_csv_file(file_path)

# Q16:
def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

input_string = input("Enter a string: ")
character_frequency = count_character_frequency(input_string)
print("Character frequency:")
for char, freq in character_frequency.items():
    print(f"'{char}': {freq}")


# Q17
def convert_to_title_case(input_string):
    return input_string.title()

input_string = input("Enter a string: ")
title_case_string = convert_to_title_case
(input_string)
print("Title case:", title_case_string)

# Q18
def are_anagrams(string1, string2):

    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    return sorted(string1) == sorted(string2)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")

# Q19:
import string

def remove_punctuation(input_string):

    translation_table = str.maketrans("", "", string.punctuation)

    return input_string.translate(translation_table)
input_string = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:", cleaned_string)

# Q20: Write a python program that takes a list of numbers and returns their sum
list=[2,3,4,5,6]
sum=0
for i in list:
    sum=sum+i
print("the sum is",sum)

# Q21:
def count_occurrences(lst, element):
    return lst.count(element)
my_list = [1, 2, 3, 4, 2, 2, 3, 5]
element_to_count = int(input("Enter the element to count occurrences for: "))
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")

# Q22:
def find_min_max(numbers):
    return min(numbers), max(numbers)

numbers = [5, 2, 8, 1, 6]
min_value, max_value = find_min_max(numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

# Q23:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Converter:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
else:
    print("Invalid choice.")

# Q24:
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator!"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print("Result:", result)
# Q25:
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully!")
    except FileNotFoundError:
        print("Error: One or both files not found.")
        
source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")

copy_file(source_file, destination_file)

# Q26:
def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix

# Example usage:
input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix)

if starts_with_prefix:
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

if ends_with_suffix:
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")

# Q27:
def string_to_list(input_string):
    return list(input_string)

input_string = input("Enter a string: ")
characters_list = string_to_list(input_string)
print("List of characters:", characters_list)

