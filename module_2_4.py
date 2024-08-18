numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
notprimes = []

for i in range(len(numbers)):
    a = numbers[i]
    k = 0
    for j in range(2, a // 2+1):
        if (a % j == 0):
            k = k+1
    if (k <= 0):
        #print("Число простое",a,'K',k)
        primes.append(a)
    else:
        #print("Число не является простым",a, 'K',k)
        notprimes.append(a)
print(primes)
print(notprimes)