def add(a,b):
        return a + b
def subtract(a,b):
        return a - b
def multiply(a,b):
        return a * b
def divide(a,b):
        if b != 0:
             return a / b
        else:
             raise ZeroDivisionError("Cannot divide by zero")
def modulo(a,b):
        if b!= 0:
             return a % b
        else:
             raise ValueError("Cannot perform modulo by zero as divisor")

while True:
	try:
                print("==================\nWelcome\nDear\nUser!\n=================")
                print("Select the operation you want to perform from 1,2,3,4,5-->")
                perform = input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulo\nPlease Enter:: ")
                if perform in ('1','2','3','4','5'):
                        num1= float(input("Please enter the first number:: "))
                        num2= float(input("Please enter the second number:: "))

                        if perform == '1':
                                  result =f"{num1} + {num2} is {add(num1,num2)}"
                        elif perform == '2':
                                  result =f"{num1} - {num2} is {subtract(num1,num2)}"
                        elif perform == '3':
                                  result =f"{num1} * {num2} is {multiply(num1,num2)}"
                        elif perform == '4':
                                  result =f"{num1} / {num2} is {divide(num1,num2)}"
                        elif perform == '5':
                                  result =f"{num1} % {num2} is {modulo(num1,num2)}"

                        print("Output of ",result)
                else:
                        print("Invalid Operation !")

                cont = input("Do you want to perform another operation? Type( *y* for Yes/ *n* for No): ")
                if cont.lower() != "y":
                        print("Calculator closed !")
                        break

	except ValueError:
              print("Invalid Input. Please enter valid numbers!")
              break
	except ZeroDivisionError:
                print("Cannot divide by zero!")
                break
	except EOFError:
                print("BYE")
                break
