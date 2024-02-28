def multi_table(n):
    for x in range(11):
        print(f'{n} * {x} = {n*x}')
        x=x+1

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
print(gcd(24,6))