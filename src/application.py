import argparse
import logging
import sys
import time

import cupy

from compute_cpu import ComputeCPU
from compute_gpu import ComputeGPU


APPLICATION_NAME = "Primality Tester 9000"


class Application:

    def __init__(self):

        args = self.parse_args()

        # Basic logging setup.
        log_level = logging.INFO
        if args.verbose:
            log_level = logging.DEBUG

        logging.basicConfig(level=log_level, force=True, stream=sys.stdout,
                            format=f"[%(asctime)s] [{APPLICATION_NAME}] [%(levelname)s] %(message)s")

        # Auto-select compute system, or allow override.
        logging.info(f"Using device: {args.device.upper()}")
        if args.device == 'gpu' and cupy.cuda.is_available():
            self._compute = ComputeGPU()
        else:
            self._compute = ComputeCPU()

        if args.INTEGER:
            self._integer = args.INTEGER

        logging.info("Initialization complete")

    def parse_args(self) -> argparse.Namespace:
        """
        Parses command line arguments/options.
        """

        parser = argparse.ArgumentParser(description=(APPLICATION_NAME))
        parser.add_argument('INTEGER', type=str, help=f'a single integer to test (max value: {sys.maxsize})')
        parser.add_argument('-d', '--device', choices=['cpu', 'gpu'], default='gpu', help='override selected compute device')
        parser.add_argument('-v', '--verbose', action='store_true', help='show more detailed logs')

        return parser.parse_args()

    def run(self) -> None:
        """
        Execute the selected compute method and display the result.
        """

        logging.info(f"Beginning primality test for '{self._integer}'")

        start_time = time.perf_counter()
        is_prime = self._compute.is_prime(self._integer)
        finish_time = time.perf_counter()

        delta_time = finish_time - start_time
        logging.info(f"Test completed in {delta_time} seconds")

        if is_prime:
            print(f"\nRESULT: {self._integer} is a prime number")
        else:
            print(f"\nRESULT: {self._integer} is not a prime number")
