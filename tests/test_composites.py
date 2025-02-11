import pytest

import lists.composites
import compute


gpu = compute.GPUCompute()

@pytest.mark.parametrize("num", lists.composites.composites)
def test_prime_numbers(num):
    assert not gpu.is_prime(num), f"Failed for {num}"
