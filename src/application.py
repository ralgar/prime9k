import argparse
import logging
import sys

from compute_gpu import ComputeGPU


APPLICATION_NAME = "Prime Tester 9000"


class Application:

    def __init__(self):

        args = self.parse_args()

        # Basic logging setup
        log_level = logging.ERROR
        if args.verbose == 1:
            log_level = logging.WARN
        if args.verbose == 2:
            log_level = logging.INFO
        if args.verbose == 3:
            log_level = logging.DEBUG

        logging.basicConfig(level=log_level,
                            format=f"[%(asctime)s] [{APPLICATION_NAME}] [%(levelname)s] %(message)s")

        self._compute = ComputeGPU()

        if args.INTEGER:
            self._integer = args.INTEGER

        logging.info("Initialization complete")

    def parse_args(self) -> argparse.Namespace:
        """
        Parses command line arguments/options.
        """

        parser = argparse.ArgumentParser(description=(APPLICATION_NAME))
        parser.add_argument('INTEGER', type=str, help=f'a single integer to test (max value: {sys.maxsize})')
        parser.add_argument('-v', '--verbose', action='count', default=0, help='increase verbosity level (-v, -vv, -vvv)')

        return parser.parse_args()

    def run(self) -> None:
        """
        Execute the main logic.
        """

        logging.debug(f"Beginning primality test for '{self._integer}'")
        is_prime = self._compute.is_prime(self._integer)
        logging.debug(f"Completed primality test for '{self._integer}'")

        if is_prime:
            print(f"\nRESULT: {self._integer} is a prime number")
        else:
            print(f"\nRESULT: {self._integer} is not a prime number")
