for sum in range(5):
    sum += sum
    print(sum)
    print("x"*9)


for x in range(5):
    print(x)
print('#'*40)

num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)