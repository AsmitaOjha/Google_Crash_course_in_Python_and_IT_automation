# 1.After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for coin in result:
    if coin=='heads':
        print("You god head")
        count=count+1
    else:
        print("you god tail")
print(count)

#2.Print square of all numbers between 1 to 10 except even numbers
for x in range(1,11,2):
    print(f'Square of {x} : {x**2}')

#3.Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
def race():
    for x in range(1,6):
        print(f"You ran {x} miles")
        answer= input("Are you tired?").lower()
        if answer=='yes':
            break
    if x==5:
        print(f"Congratulation you ran {x}km")
    else:
        print(f"You didn't finish the race, anyway you run {x} km")

race()

#Write a program that prints following shape

# *
# **
# ***
# ****
# *****
# n=int(input("Enter any integer number: "))
# for x in range(n+1):
#     print('*'*x)
# #solution
for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)


            



