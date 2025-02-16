import math
import multiprocessing

from compute.compute_base import ComputeBase


class ComputeCPU(ComputeBase):
    """
    Derived class for a compute system.
    """

    def is_prime(self, n: int) -> bool:
        """
        Test whether n is prime using a CPU-parallelized 6k±1 algorithm.
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

        # Break work down into batches, and submit to multiprocessing pool.
        sqrt_n = math.isqrt(n)
        batch_size = 1_000_000
        num_workers = multiprocessing.cpu_count()

        with multiprocessing.Pool(num_workers) as pool:
            tasks = []
            for start in range(5, sqrt_n + 1, batch_size):
                end = min(start + batch_size, sqrt_n + 1)
                tasks.append((n, start, end))

            # Execute
            results = pool.starmap(self.is_prime_batch, tasks)

            # If any batch finds a factor, the number isn't prime.
            if not all(results):
                return False

        # If no factor is found, the number is prime.
        return True

    def is_prime_batch(self, n: int, start: int, end: int) -> bool:
        """
        Checks if `n` is divisible in the range of start to end, using the
        6k +/- 1 method. This method works on the basis that all prime numbers
        above 3 must of the form 6k +/- 1, as 6k +/- 2/3/4 are always divisible
        by either 2 or 3.
        """

        for i in range(start, end, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True
