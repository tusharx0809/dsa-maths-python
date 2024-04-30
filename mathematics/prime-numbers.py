#Program to check if a number is prime

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

primes = []
for num in range(1,100):
    if is_prime(num):
        primes.append(num)

print(primes)

        