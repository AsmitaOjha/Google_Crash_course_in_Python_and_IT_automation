def count_letters(name):
    result ={}
    for letter in name:
        if letter not in result:
            result[letter]=0
        result[letter]+=1
    return result

name= input("Enter your name without space: ").lower()
print(count_letters(name))