def to_celsius(x):
    return (x-32)*(5/9)

for x in range (-50,101,10):
    # print(x, to_celsius(x))
    print("{:<3}F | {:>6.2F} C".format(x,to_celsius(x)))

