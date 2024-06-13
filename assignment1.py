#                                           ASSIGNMENT- 1

#q1- Write a program that takes two numbers as input and prints their sum
'''a = int(input("Enter first number: "))
b= int(input("enter second number: "))
print("Sum of two  numbers is : ", a+b)'''
#q2- Write a python program that checks whether a given number is even or odd
'''def evenOrOdd(number):
    if(number%2==0):
        print("It is Even Number.")
    
    else:
        print("It is an Odd Number.")
no = int(input('Enter a Number : '))
evenOrOdd(no)'''
#q3- Write a python program that calculates the factorial of a given number. 
'''def factorial(num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial
a=5
print("The factorial is ", factorial(a))'''
#q4-Write a program that asks the user for their name and then prints a greeting messsage
'''name = input("Enter your name ")
print("Have a Good Day ",  name)'''
#q5- Write a program that takes a string input from the user and writes it to a text file
'''f = input("Enter the text you want to write to the file: ")
filename = "C:\\Users\\vikra\\OneDrive\\Desktop\\Desktop\\python& ml\\Homework\\file1.txt"
with open(filename, 'w') as file:
    file.write(f)
print("The text has been written to ", filename)'''
#q6-Write a program that reads the content of a text file and prints it to the console
'''filename = "C:\\Users\\vikra\\OneDrive\\Desktop\\Desktop\\python& ml\\Homework\\file1.txt"
try:
    with open(filename, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")'''
#q7-Write a python program that takes a string as input and returns its length.
'''str = input("Enter a string ")
print("The length of string is ", len(str))'''
#q8-Write a python program that concatenates two strings and returns the result.
'''def concate(a,b):
    return a+b
a = input("First String ")
b = input("Second String ")
print("After concatenation ", concate(a,b))'''
#q9-Write a python program that checks if a substring is present in a given string. 
'''def substr(substring, main_string):
    if substring in main_string:
        print(f"The substring '{substring}' is present in the main string.")
    else:
        print(f"The substring '{substring}' is not present in the main string.")
main_string = input("Enter a string ")
substring =input("String which you want to check ")
substr(substring, main_string)'''
#q10-Write a python program that converts a given string to uppercase. 
'''a = "Hello"
upper_a= a.upper()
print("String converted ", upper_a)'''
#q11-Write a python program that generates the first n numbers in the Fibonacci sequence.
'''def fibonacci(n):
    num2 = 1
    next_number = num2  
    count = 1
    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        print()
n= int(input("Enter a number "))
fibonacci(n)'''
#q12-Write a python program that calculates the sum of the digits of a given number
'''def sumofdigits(no):
    sum=0
    while(no!=0):
        dig = no%10
        sum +=  dig
        no = no//10
    print("Sum of digits ",sum)
no= int(input("Enter a  number "))
sumofdigits(no)'''
#q13- Write a program that asks the user for their birth year and calculates their age. 
'''year = int(input("Enter your birth year "))
print("Current Age ", 2024-year)'''
#q14-Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
'''def read_and_print_lines():
    lines = [] 
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    print("You entered:")
    for line in lines:
        print(line)
read_and_print_lines()'''
#q15-Write a program that reads data from a CSV file and prints it to the console.
'''import csv
def read_and_print_csv(file_path):
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(', '.join(row))
csv_file_path = "C:\\Users\\vikra\\OneDrive\\Desktop\\Desktop\\python& ml\\Homework\\csv1.csv"
read_and_print_csv(csv_file_path)'''
#q16-Write a program in python that counts the frequency of each character in a string
'''def counts(a):
    all_freq = {}
    for char in a:
        if char in all_freq:
            all_freq[char] += 1
        else:
            all_freq[char] = 1
    return all_freq
a ="banana"
print(counts(a))'''
#q17-Write a program in python that converts a given string to title case (first letter of each word capitalized). 
'''a ="india's national bird is peackock."
print(a.title())'''
#q18-Write a python program that checks if two strings are anagrams of each other. 
'''def anagram(a,b):
    str1= a.lower()
    str2= b.lower()
    if(len(str1)== len(str2)):
        s_str1= sorted(str1)
        s_str2= sorted(str2)
        s_str1==s_str2
        return True
    return False
a ="evil"
b = "vile"
print("It is anagram: ", anagram(a, b))'''
#q19-Write a python program that removes all punctuation from a given string.
'''def delpunc(a):
    punctuations = "!()-[];:'\/<>.,/?@#$%^&*_~"
    cleaned_str = ""
    for char in a:
        if char not in punctuations:
            cleaned_str += char
    return cleaned_str
a="We, are living$ in .;21st] centuary."
print("After deleting punctuations: ", delpunc(a))'''
#q20-Write a python program that takes a list of numbers and returns their sum.
'''def sum_of_list(l):
    sum=0
    for i in range(len(l)):
        sum+= l[i]
    return sum
l = [1,5,6,7,3,9,2]
print("Sum of all numbers of list is ", sum_of_list(l))'''
#q21-Write a python program that counts the occurrences of a specific element in a list. 
'''l = [1, 3, 4, 5, 6, 2, 5, 9, 7, 4 , 5]
target=5
print("Count of tareget ", l.count(target))'''
#q22-Write a python program that returns the minimum and maximum values in a list of numbers. 
'''def max_min(l):
    print("Maximum of list is ", max(l))
    print("Minimum of list ", min(l))
l = [1, 3, 4, 5, 6, 2, 5, 9, 7, 4 , 5]
max_min(l)'''
#q23-Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
'''def temp_change(a,b):
    temp =0
    if(b== 'C' or b=='c'):
        print("Current temperature is ", a, "  degree Celcius.")
        temp =((9/5)*a)+32
        print("Temperature in Fahrenheit is ", temp,"degree fahrenheit.")
    else:
        print("Current temperature is ", a, "degree Fahrenheit")
        temp = (a-32)*(5/9)
        print("Temperature in celcius is ", temp,"degree Celcius.")
a = float(input("Enter temperature degree "))
b = input("Enter 'C' or 'c' for Celcius or 'F' or'f' for Fahrenheit ")
temp_change(a,b)'''
#q24-Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result
'''def calculator(a, b, c):
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=="/":
        return a/b
    else:
        return "Invalid Input. Try Again"
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c = input("Enter an operator from  (+, -, *, /): ")
print("Result is : ", calculator(a,b,c))'''
#q25-Write a program that copies the contents of one text file to another. 
'''with open('C:\\Users\\vikra\\OneDrive\\Desktop\\Desktop\\python& ml\\Homework\\first.txt', 'r') as firstfile, open("C:\\Users\\vikra\\OneDrive\\Desktop\\Desktop\\python& ml\\Homework\\second.txt", 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
    print("File copied successfully.")'''
#q26-Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
'''def checks_substr(a,b, c):
    if c == "prefix":
        return a.startswith(b)
    elif c== "suffix":
        return a.endswith(b)
    else:
        return "Invalid input"

a= "Hello, world!"
c=input("Enter 'prefix' or 'suffix' ")
b = "Hello"
print(checks_substr(a,b,c))'''
#q27-Write a program in python that converts a string into a list of its characters.
'''def char_to_list(str):
    lst =[]
    for i in range(len(str)):
        lst.append(str[i])
    return lst
str="apple"
print("List of string is ", char_to_list(str))'''


