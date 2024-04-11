#    Create Generator method such that every time it will returns a next square number

#for exmaple : 1 4 9 16 ..
def next_square():
    i=1
    while True:
        yield i*i
        i+=1

for n in next_square():
    if n>100:
        break
    print(n)

     