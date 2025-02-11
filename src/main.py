# Brute Force Primality Checker
# Checks a given number for primality, using a multi-threaded,
#  brute force 6k +/- 1 algorithm.
#
# Copyright (c) 2025 Ryan Algar
# This work is released to the public domain under CC0 1.0


import sys

from application import Application


def main() -> None:
    """
    Program entrypoint.
    """

    try:
        app = Application()
        app.run()
    except KeyboardInterrupt:
        print("\nInterrupt caught! Exiting gracefully.")
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
