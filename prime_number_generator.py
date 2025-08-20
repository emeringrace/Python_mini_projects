def sieve(limit):
    if limit < 2:
        raise ValueError("Invalid input.")
    primes =[True] * (limit + 1)
    primes[0] = primes[1] = False  
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    
    return [num for num in range(2, limit + 1) if primes[num]]
