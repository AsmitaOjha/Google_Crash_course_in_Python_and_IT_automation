f=open("E:/Programming/Crash Course of Python by Google/json files for my practice/book.txt",'r')
s=f.read()
print(s)
print(type(s))
import json
book= json.loads(s)
print(book)
print(type(book))
print(book['bob'])
print(book['bob']['phone'])
for person in book:
    print(book[person])