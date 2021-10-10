__version__ = '0.1.0'

import argparse

import pendulum


def parse():
    parser = argparse.ArgumentParser(description="Print current date and time for a timezone")
    parser.add_argument("-tz" ,"--timezone", default="UTC")
    return parser.parse_args()


def now(timezone):
    return pendulum.now(timezone)


def main():
    args = parse()
    print(now(args.timezone))


if "__name__" == "__main__":
    main()
