#!/usr/bin/env python3
"""Commands to control the pi-cluster."""

#stand lib
import argparse as ap
import subprocess

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
    """Determines validity. Returns Boolean."""
    return value in valid_args

def format_command(arg):
    """Formats the command. Returns String."""
    if valid(arg):
        cmd = "pi"+arg
        return cmd

def _reboot(cluster):
    """Reboots all the nodes in cluster. Returns None."""
    clear_terminal()
    for pi in cluster:
        command = "ssh pi@"+pi+" 'sudo reboot'"
        print("command ::", command)
        c = subprocess.Popen(command, encoding='utf-8', 
                             stdout=subprocess.PIPE, shell=True)
        pi_outputs.append(c.stdout)

# Main
parser = ap.ArgumentParser(description="Commands for the pi-cluster.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-r", "--reboot", help="Reboots the cluster.", 
    nargs="?",const=["0", "1", "2", "3"])
group.add_argument("-s", "--shutdown", help="Shuts down the cluster.",
    nargs="?",const=["0", "1", "2", "3"])

# not needed
#group.add_argument("-s", "--shutdown", help="Shutdown the cluster.", 
#    action="store_true")
#group.add_argument("--rebootpi", help="Reboots a single pi.")
#group.add_argument("--shutdownpi", help="Shutdown a single pi.")

args = parser.parse_args()

if args.reboot:
#    for arg in given_args[0]:
#        if arg!=None:
#            print(format_command(arg))
    print(args.reboot)
elif args.shutdown:
#    for arg in given_args[0]:
#        if arg!=None:
#            print(format_command(arg))

    print(args.shutdown)
for _, value in args._get_kwargs():
    given_args.append(value)
    print(_, "::", value)

#print("given_args::", given_args)

#for arg in given_args[0]:
#    if arg!=None:
#        print(format_command(arg))
