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
parser.add_argument("square", help="display the square of a given number.", type=int)

# optional argument
parser.add_argument("-v", "--verbose", help="display verbose messages.", action="store_true")

args = parser.parse_args()

#this just "echoes" the argument passed in from the command line
#print(args.echo)

#print(args.square**2)


answer = args.square**2
if args.verbose:
#    print("some extra verbosity")
    print("The square of {} is {}".format(args.square, answer))

