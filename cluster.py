#!/usr/bin/env python3
"""Commands to control the pi-cluster."""

#stand lib
import argparse as ap
import subprocess
from time import sleep

#custom
from pi_ipaddresses import *

cluster     = [pi0, pi1, pi2, pi3]      # ip addresses
pi_outputs  = []                        # holds stdout from pis
valid_args  = ["", "0", "1", "2", "3"]
given_args  = []                        # holds args from command line

def clear_terminal():
    """Clears the terminal window. Returns None."""
    subprocess.run(["clear"])

def show_outputs():
    """Shows the outputs of the pis. Returns None."""
    for output in pi_outputs:
        print(str(pi_outputs.index(output)), "::", output)

def valid(value):
    """Determines validity of arguments. Returns Boolean."""
    #if all values are in valid args and the length of the argument list is
    #+ equal to or less than valid_args
    return value in valid_args

def format_pi_name(arg):
    """Formats the command. Returns String."""
    cmd = "pi@"+arg
    return cmd

def print_kwargs():
    """Displays kwargs given at command line. Returns None."""
    for _, value in args._get_kwargs():
        given_args.append(value)
        print(_, "::", value)

def print_pi_outputs():
    """Displays contents of pi_outputs. Returns None."""
    [print(out.stdout) for out in pi_outputs]

def _reboot(pi):
    """Reboots all the nodes in cluster. Returns None."""
    name = format_pi_name(cluster[int(pi)])
    cmd = "ssh "+name+" 'sudo reboot'"
    c = subprocess.Popen(cmd, encoding='utf-8', 
                         stdout=subprocess.PIPE, shell=True)
    pi_outputs.append(c.stdout)
#    print(cmd)

def _shutdown(pi):
    """Shutsdown all the nodes in cluster. Returns None."""
    name = format_pi_name(cluster[int(pi)])
    cmd = "ssh "+name+" 'sudo shutdown -h now'"
    c = subprocess.Popen(cmd, encoding='utf-8', 
                         stdout=subprocess.PIPE, shell=True)

def _name(pi):
    """Gets the name of the machine. Returns String."""
    name = format_pi_name(cluster[int(pi)])
    cmd = "ssh "+name+" 'hostname'"
    c = subprocess.Popen(cmd, encoding='utf-8',
                         stdout=subprocess.PIPE, shell=True)
    for line in c.stdout:
        print(line.strip())

# Main
parser = ap.ArgumentParser(description="Commands for the pi-cluster.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-r", "--reboot", help="Reboots the cluster.", 
    nargs="?",const=["0", "1", "2", "3"])
group.add_argument("-s", "--shutdown", help="Shuts down the cluster.",
    nargs="?",const=["0", "1", "2", "3"])
group.add_argument("-n", "--name", help="Displays the name of the node.",
    nargs="?",const=["0", "1", "2", "3"])

args = parser.parse_args()
clear_terminal()

#newline for nice output format
print("\n")

if args.reboot:
    [_reboot(arg) for arg in args.reboot]
elif args.shutdown:
    [_shutdown(arg) for arg in args.shutdown]
elif args.name:
    [_name(arg) for arg in args.name]


# End program
parser.exit(status=0, message="Finished.\n")
