string1 = "Greetings, Earthlings"
print(string1[0])
#G
print(string1[0:10])
#Greetings, #not included 10th index.
print(string1[-8:])
#rthlings
print(string1[:-5])

#stride argument
print(string1[0::2])
#Getns atlns
print(string1[::-1])
#sgnilhtraE ,sgniteerG
print(string1[::-2])


#common error: 
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends("Barry")
#solved in this way 
greet_friends(["Barry"])

#assignment question:
for sum in range(5):
    sum += sum
    print(sum)