def to_celsius(x):
    return (x-32)*(5/9)

for x in range (-50,101,10):
    print(x, to_celsius(x))