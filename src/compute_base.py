from abc import ABC, abstractmethod
import logging


class ComputeBase(ABC):
    """
    Abstract base class for a compute system.
    """

    def __init__(self):
        logging.info("Compute initialized")
        pass

    @abstractmethod
    def is_prime(self, n: int) -> bool:
        """
        Test whether n is prime using a CPU or GPU parallelized 6k±1 algorithm.
        This function uses CuPy to generate batches of candidate divisors
        (of the form 6k-1 and 6k+1) and checks in parallel if any divide n.

        Parameters:
            n (int): The number to test (as a Python integer).

        Returns:
            bool: True if n is prime, False otherwise.
        """

        pass
