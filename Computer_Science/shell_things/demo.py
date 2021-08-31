prime_numbers = []

def find_primes():
    x = [False, False]
    x = x + [True]*(10**6)
    
    for i in range(2, len(x)):
        if x[i]:
            j = 2
            while i*j < len(x):
                x[i*j] = False
                j+=1
            prime_numbers.append(i)
    print(prime_numbers)

find_primes()
