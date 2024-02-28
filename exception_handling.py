x = input("Enter first number: ")
y=input("Enter second number: ")
try:
    z= x/int(y)
except ZeroDivisionError as e:
    print("Division by zero exception")
    z=None
# except Exception as e:
#     print('exception type: ', type(e).__name__)
except TypeError as e:
    print('Type error exception')
    z=None
print("Division is: ",z)