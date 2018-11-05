#!/usr/bin/env python3
"""Argument Parser tutorial from;
    https://docs.python.org/3/howto/argparse.html#id1
"""


import argparse

parser = argparse.ArgumentParser(description="")

# "echo" is the "key" that holds the argument that you will put in its 
#+ position. This is a positional argument.

# string as argument
#parser.add_argument("echo", help="echo the string that you put here.")

# integer as argument
#parser.add_argument("square", help="display the square of a given number.", type=int)

# optional argument
parser.add_argument("--verbose", help="display verbose messages.")

args = parser.parse_args()

#this just "echoes" the argument passed in from the command line
#print(args.echo)

#print(args.square**2)

if args.verbose:
    print("some extra verbosity")

