import sympy

def generate_primes(length: int, start: int = 1):
    primes = []
    k = start  # Set the start point for k

    while len(primes) < length:
        for offset in [-1, 1]:        # Generate 6k +/- 1
            num = 6 * k + offset
            if sympy.isprime(num):    # Check if prime
                primes.append(num)
        k += 1

    return primes

primes = []

primes.extend(generate_primes(1_000, 1))
primes.extend(generate_primes(1_000, 1_000))
primes.extend(generate_primes(1_000, 1_000_000))
primes.extend(generate_primes(1_000, 1_000_000_000))
primes.extend(generate_primes(1_000, 1_000_000_000_000))
primes.extend(generate_primes(1_000, 1_000_000_000_000_000))
primes.extend(generate_primes(1_000, 1_000_000_000_000_000_000))

print(primes)
