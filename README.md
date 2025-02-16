# Primality Tester 9000 (prime9k)

## Overview

A brute force primality testing program written in Python. It uses a 6k +/- 1
 algorithm, that is parallelized using either the CPU or GPU (depending on
 what's available/selected).

## Manual Installation

### Requirements

- `python>=3.8,<3.13`
- `pip`
- CUDA (optional, for GPU acceleration)

### Installation

1. Clone this repository, and change directory.

   ```sh
   $ git clone https://github.com/ralgar/prime9k.git
   $ cd prime9k
   ```

1. Create and activate a virtual environment.

   ```sh
   $ python -m venv venv
   $ source venv/bin/activate
   ```

1. Install the Python package.

   ```sh
   $ pip install .
   ```

### Usage

1. Invoke the help dialog to learn how to use the program.

   ```text
   $ prime9k --help
   usage: prime9k [-h] [-d {cpu,gpu}] [-v] INTEGER

   Primality Tester 9000

   positional arguments:
     INTEGER               a single integer to test (max value: 9223372036854775807)

   options:
     -h, --help            show this help message and exit
     -d {cpu,gpu}, --device {cpu,gpu}
                           override selected compute device
     -v, --verbose         show more detailed logs
   ```

## Running with Docker

If you don't want to mess with venvs and dependencies, a single-command Docker
 Compose build is provided.

### Requirements

- Docker
- NVIDIA Container Toolkit (optional, for GPU acceleration)

### Usage

1. Build and start the container using Docker Compose.

   ```sh
   $ docker compose --profile [cpu,gpu] up
   ```

1. Once the program has finished execution, bring the compose stack down.

   ```sh
   $ docker compose --profile [cpu,gpu] down
   ```

## Tests

Prime9k comes with a dynamic testing framework that leverages a well-known
 algebra library ([SymPy](https://www.sympy.org/en/index.html)) to generate
 valid prime and composite numbers at runtime. A wide range of values are
 tested (over **20,000** combined prime and composite numbers), and both the
 CPU and GPU compute algorithms are tested.

After following the [Manual Installation](#manual-installation) steps:

1. Install the `test` optional dependencies.

   ```sh
   $ pip install .[test]
   ```

1. Invoke `pytest` from the project root.

   ```sh
   $ pytest
   ```

## License

Copyright: (c) 2025, Ryan Algar
 ([ralgar/prime9k](https://gitlab.com/ralgar/prime9k))

BSD 2-clause License (see [LICENSE](LICENSE) or
 [BSD 2-clause](https://choosealicense.com/licenses/bsd-2-clause/))
