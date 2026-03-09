# Drill 9: Count Primes (Sieve of Eratosthenes)
# Not strictly hashing, but uses highly analogous boolean array lookup

def count_primes(n):
    if n <= 2: return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
                
    return sum(is_prime)

if __name__ == "__main__":
    print(count_primes(10)) # Expected: 4
