"""Command-line interface to pycat."""

import argparse
import sys


def argument_parser():
    """Generate an `argparse` argument parser for pycat's arguments."""
    parser = argparse.ArgumentParser(description='netcat, in Python')
    parser.add_argument('hostname', help='host to which to connect')
    parser.add_argument('port', help='port number to which to connect')
    return parser


def main(args=sys.argv[1:]):
    """Run, as if from the command-line.

    args is a set of arguments to run with, defaulting to taking arguments from
    `sys.argv`. It should **not** include the name of the program as the first
    argument.
    """
    parser = argument_parser()
    args = parser.parse_args(args)
    print(args)
