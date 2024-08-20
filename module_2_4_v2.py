numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
notprimes = []


for i in numbers:
    is_prime = True
    # print('i', i)
    if i < 2:
        continue
    else:
        k = i ** (1/2)
    for j in range(2, int(k+1)):
        # print('i', i, 'j',j,'K',k)
        if (i % j == 0):
            is_prime = False
            break
    if not (is_prime):
        #print("Число простое",i)
        notprimes.append(i)
    else:
        #print("Число не является простым",i)
        primes.append(i)
is_prime = True
print(primes)
print(notprimes)


