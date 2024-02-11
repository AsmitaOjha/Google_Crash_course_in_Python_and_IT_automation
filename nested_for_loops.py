for left in range(7):
    # print(left)
    for right in range(left,7):
        # print(right)
        # print("x"*right)
        print('['+ str(left)+ '|'+str(right)+ ']',end='')
    print()
    
teams = ['Dragons','Wolves','Pandas','Unicorns'] 
for home_team in teams:
    # print(home_team)
    # print("x")
    for away_team in teams:
        # print(away_team)
        if home_team!=away_team:
            print(home_team + '🆚 '+ away_team)

#looping over a string
greeting="Good Morning"
for i in range(len(greeting)):
	print(i)

for i in greeting:
     print(i)
print("*"*9)

i=0
while i<len(greeting):
     print(greeting[i])
     i +=1
print("#"*8)

#list comprehensions
numbers = [1,3,5,7,9]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)


#map() function
def square(x):
     return x*x

numbers = [1,2,3,4,5]
sqrs_of_numbers = map(square, numbers)
next(sqrs_of_numbers)

#zip() function
numbers = [1,2,3]
str_numbers = ['One','Two','Three']
result = zip(numbers, str_numbers)
print(result)
print(list(result))