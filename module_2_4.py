numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for j in numbers:
    is_prime = True
    if j < 2:
        is_prime = False
    else:
        for i in primes:
            if j % i == 0:
                is_prime = False
                break
        
    if is_prime:
        primes.append(j)
    else:
        not_primes.append(j)
if 1 in primes:
    primes.remove(1)
if 1 in not_primes:
    not_primes.remove(1)
print("Простые числа: ", primes)
print("Не простые числа: ", not_primes)
