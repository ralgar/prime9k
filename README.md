# Prime Tester 9000

## Overview

A brute force primality testing program written in Python. It uses a 6k +/- 1
 algorithm, that is parallelized using either the CPU or GPU (depending on
 what's available).

## Getting Started

### Installation

1. Clone this repository, and change directory.

   ```sh
   git clone https://github.com/ralgar/prime9k.git
   cd prime9k
   ```

1. Create a virtual environment using your preferred method.

   ```sh
   python -m venv venv
   ```

1. Install the Python package.

   ```sh
   pip install .
   ```

### Usage

1. Invoke the help dialog to learn how to use the program.

   ```sh
   prime9k --help
   ```

## Tests

The project comes with a dynamic testing framework that leverages a well-known
 algebra library ([SymPy](https://www.sympy.org/en/index.html)) to generate
 valid prime and composite numbers at runtime. A wide range of values are
 tested, and both the CPU and GPU algorithms are covered.

1. Install the `test` optional dependencies.

   ```sh
   pip install .[test]
   ```

1. Invoke `pytest` from the project root.

   ```sh
   pytest
   ```

## License

Copyright: (c) 2025, Ryan Algar
 ([ralgar/prime9k](https://gitlab.com/ralgar/prime9k))

BSD 2-clause License (see [LICENSE](LICENSE) or
 [BSD 2-clause](https://choosealicense.com/licenses/bsd-2-clause/))
