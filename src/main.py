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
