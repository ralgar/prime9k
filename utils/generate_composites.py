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

composites = []

composites.extend(generate_composites(1_000, 1))
composites.extend(generate_composites(1_000, 1_000))
composites.extend(generate_composites(1_000, 1_000_000))
composites.extend(generate_composites(1_000, 1_000_000_000))
composites.extend(generate_composites(1_000, 1_000_000_000_000))
composites.extend(generate_composites(1_000, 1_000_000_000_000_000))
composites.extend(generate_composites(1_000, 1_000_000_000_000_000_000))

print(composites)
