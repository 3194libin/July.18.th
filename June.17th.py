import math
def calculate(a,b,c):
    if b*b-4*a*c<0:
        print("error")
    if b*b-4*a*c==0:
        print("only one")
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
        return x1,x2

a = input()
b = input()
c = input()
d = calculate(a,b,c)
print(d)