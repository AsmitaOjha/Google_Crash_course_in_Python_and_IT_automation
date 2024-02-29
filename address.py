book ={}
book['tom']={
    'name':'tom',
    'address': '1 red street, NY',
    'phone':98989898
}
book['bob']={
    'name':'bob',
    'address':'1 green street,NY',
    'phone': 234567879
}
print(book)
import json 
s=json.dumps(book)
#dictionary object taking and dumping as a string which will be in json format
print(s)
with open('E:/Programming/Crash Course of Python by Google/json files for my practice/book.txt','w') as f:
    f.write(s)