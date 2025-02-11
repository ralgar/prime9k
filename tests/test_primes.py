import pytest

import lists.primes
import compute


gpu = compute.GPUCompute()

@pytest.mark.parametrize("num", lists.primes.primes)
def test_prime_numbers(num):
    assert gpu.is_prime(num), f"Failed for {num}"
