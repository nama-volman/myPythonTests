#DAY 1 EXERCISE:


# print("Hello, World!");
# print(int("3")+5)
# name=input("What is your name? ")
# print("Hello, " + name + "!")
# a= int (input("Enter a number: "))
# b= int (input("Enter another number: ")) 
# c= int (input("Enter a third number: "))
# d= a * b *c
# print ("The product of your three numbers is: " + str(d))
# print(type(name))
# print(type(True))
# print(type(8))
# print(type(5.3))
# print(type("smart"))
# print (0>1)
# print (1<3)
# print (3<4)
# print (5<=5)
# print (1<=5)
# print ("smart"=="Smart")
# print ("smart"=="smart")
# a=(1<3)
# b=(3>4)
# print (a==b)

# a =50
# print ("Decimal: " + str(a) )
# print ("Octal: " + oct(a))
# print ("Hexadecimal: " + hex(a))
# print ("Binary: " + bin(a))



# This program prompts the user to enter their first and last name, then greets them and displays the data types of the inputs.

# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# print("Hello " + firstName + " " + lastName + "!")
# print ( "type of firstName: " + str(type(firstName)) )
# print ( "type of lastName: " + str(type(lastName)) )


# This program prompts the user to enter two numbers and an operator, then performs the corresponding arithmetic operation and displays the result.

# x = input("Enter a number:")
# operator = input("Enter an operator (+, -, *, /): ")
# y = input("Enter another number: ")

# if operator == "+":
#     result = float(x) + float(y)
# elif operator == "-":
#     result = float(x) - float(y)
# elif operator == "*":
#     result = float(x) * float(y)
# elif operator == "/":
#     try:
#         result = float(x) / float(y)
#     except ValueError:
#         result = "Error: Invalid input. Please enter valid numbers."    
#     except ZeroDivisionError:
#         result = "Error: Division by zero is not allowed."
#     #except Exception as e:
#     #    result = f"An unexpected error occurred: {e}"
# else:
#     result = "Invalid operator"
# print ("The result of " + x + " " + operator + " " + y + " is: " + str(result))


# This program demonstrates the use of try-except blocks to handle exceptions when performing operations on different data types.

# z= 7
# W = "5.3"
# try :
#     u= int(W)
#     print (u)
# except ValueError:
#     print("Error: Cannot convert this string to integer.")
# else:
#     print("Conversion successful.")
# finally:
#     print("Execution completed.")

# try:
#     v= z + W
# except TypeError:
#     print("Error: Cannot add an integer and a string.")
# else:
#     print("Addition successful.")
# finally:
#     print("Execution completed.")

# try:
#     print(z.lower())
# except AttributeError:
#     print("Error: The variable z is not a string.")
# else:
#     print("Lowercase conversion successful.")
# finally:
#     print("Execution completed.")


# This program demonstrates the use of different fanctoins.

#num = float (input("Enter a number:"))
#print (num)
# print (type(str(num)))
# string = input("Enter a string:")
# print (len (string))


