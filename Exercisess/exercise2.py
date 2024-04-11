# #Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print

# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
#def print_pattern(x):
#     for x in range(x+1):
#         print("*"*x)

#print_pattern(3)

#alternative way
def print_pattern(n=5):
    '''
    :param n: Integer number representing number of lines
    to be printed in a pattern. If n=3 it will print,
      *
      **
      ***
    If n=4, it will print,
      *
      **
      ***
      ****
    Default value for n is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
    '''
    # we need to run two for loops. Outer loop prints patterns line by line
    # where as inner loop print the content of that specific lines
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)

print_pattern(8)