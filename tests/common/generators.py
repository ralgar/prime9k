import random
import sys

import sympy


def generate_composites(length: int, start: int = 1):
    composites = []
    k = start  # Set the start point for k

    while len(composites) < length:
        for offset in [-1, 1]:            # Generate 6k +/- 1
            num = 6 * k + offset
            if not sympy.isprime(num):    # Check if composite
                composites.append(num)
        k += 1

    return composites


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


def generate_random_number(length: int) -> int:
    """
    Generate a random integer with a given length.
    """

    # Get the max value/length for a C long
    max_long_value = sys.maxsize
    max_length = len(str(max_long_value))

    if length == 1:
        return random.randint(0, 9)  # For a single digit, range is 0-9
    if length > max_length:
        raise Exception(f"Requested length '{length}' will exceed the size of a C long on this system.")

    # Set upper and lower bounds such that we can multiply by 6 without exceeding
    #  the defined length. Ex. length = 4, lower = 1000, upper = 1500.
    lower_bound = 10 ** (length - 1)
    upper_bound = round(10 ** (length - 1) * 1.5)

    # Generate the random number in the given range
    return random.randint(lower_bound, upper_bound)
