#this is to perfom error handling, we will do try, except, else and finally.

# try and except block to catch errors
# else block to run the code, and safely escape the first tril and make 2nd statement run.

# finally block to run code regardless of the try and except block.

try :
    # code that may raise an error
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")