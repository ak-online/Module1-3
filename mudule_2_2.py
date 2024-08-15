a = input('First Number : ')
b = input('Second Number : ')
c = input('Third Number : ')
if a == b and a == c:
    print (3)
elif a== b or a == c or b == c:
    print(2)
if not a== b and not a == c and not b == c:
    print(0)