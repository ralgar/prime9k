from typing import List

import pytest

from common.generators import generate_primes, generate_random_number
from compute_gpu import ComputeGPU


gpu = ComputeGPU()


def setup_data() -> List[int]:
    data = []

    data.extend(generate_primes(1_000, 1))
    data.extend(generate_primes(1_000, generate_random_number(4)))
    data.extend(generate_primes(1_000, generate_random_number(7)))
    data.extend(generate_primes(1_000, generate_random_number(10)))
    data.extend(generate_primes(1_000, generate_random_number(13)))
    data.extend(generate_primes(1_000, generate_random_number(16)))
    data.extend(generate_primes(1_000, generate_random_number(19)))

    return data


@pytest.mark.parametrize("num", setup_data())
def test_prime_numbers(num):
    assert gpu.is_prime(num), f"Failed for {num}"
