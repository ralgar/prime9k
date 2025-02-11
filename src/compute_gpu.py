import logging
import math

import cupy as cp

from compute_base import ComputeBase


class ComputeGPU(ComputeBase):
    """
    Derived class for a compute system.
    """

    def __init__(self):
        logging.info(f'Using CuPy version: {cp.__version__}')

    def is_prime(self, n: int) -> bool:
        """
        Test whether n is prime using a GPU-parallelized 6k±1 algorithm.
        This function uses CuPy to generate batches of candidate divisors
        (of the form 6k-1 and 6k+1) and checks in parallel if any divide n.

        Parameters:
            n (int): The number to test (as a Python integer).

        Returns:
            bool: True if n is prime, False otherwise.
        """

        n = int(n)

        # Handle simple cases directly.
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        # Compute the integer square root of n.
        sqrt_n = math.isqrt(n)

        # Convert n to a 64-bit cp integer for GPU computations.
        n_cp = cp.int64(n)

        # Process candidate divisors in batches of 1,000,000.
        batch_size = 1_000_000
        offset = 0

        while True:
            # Create a batch of indices on the GPU.
            indices = cp.arange(offset, offset + batch_size, dtype=cp.int64)

            # For each index i, compute k = (i // 2) + 1.
            k = (indices // 2) + 1

            # Compute candidate divisors:
            #   - If i is even: candidate = 6*k - 1
            #   - If i is odd:  candidate = 6*k + 1
            candidates = cp.where(indices % 2 == 0, 6 * k - 1, 6 * k + 1)

            # Filter out candidates that are greater than sqrt(n)
            valid_candidates = candidates[candidates <= sqrt_n]

            # If no valid candidate remains in this batch, we're done.
            if valid_candidates.size == 0:
                break

            # Check in parallel: if any candidate divides n exactly, then n is composite.
            # Using cp.any().item() converts the result to a Python bool.
            if cp.any(n_cp % valid_candidates == 0).item():
                return False

            # If this batch did not produce a full set of 1,000,000 valid candidates,
            # then we've reached beyond sqrt(n) and can finish checking.
            if valid_candidates.size < batch_size:
                break

            # Otherwise, move to the next batch.
            offset += batch_size

        # If no divisor was found, n is prime.
        return True
