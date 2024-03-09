#OLd method to open and close files
# poem =open('demo.txt','r')
# for line in poem:
#     print(line, end='')

# poem.close()
#Using with to open and read line
# with open('demo.txt','r') as poem:
#     for line in poem:
#         print(line.rstrip())

#using readlines()
#returns a list containing all lines 
# with open('demo.txt','r') as poem:
#     lines= poem.readlines()
# print(lines)

#using read() method
#returns a string containing all lines
# with open('demo.txt','r') as poem:
#     text=poem.read()
# print(text)
# print(type(text))

# for character in reversed(text):
#     print(character,end='')

#using readline()
with open('demo.txt','r') as poem:
    while True:
        line=poem.readline().rstrip()
        print(line)
        if 'dead' in line.casefold():
            break;


