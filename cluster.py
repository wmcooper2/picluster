#!/usr/bin/env python3
"""Commands to control the pi-cluster."""

#stand lib
import argparse as ap
import subprocess

#custom
from pi_ipaddresses import *

pis         = [pi0, pi1, pi2, pi3]
pi_outputs  = []

def clear_terminal():
    """Clears the terminal window. Returns None."""
    subprocess.run(["clear"])

def show_outputs():
    """Shows the outputs of the pis. Returns None."""
    for output in pi_outputs:
        print(str(pi_outputs.index(output)), "::", output)

def _reboot(pis):
    """Reboots all the nodes in pis. Returns None."""
    clear_terminal()
    for pi in pis:
        command = "ssh pi@"+pi+" 'sudo reboot'"
        print("command ::", command)
        c = subprocess.Popen(command, encoding='utf-8', 
                             stdout=subprocess.PIPE, shell=True)
        pi_outputs.append(c.stdout)
        #call named pipe command
        #save the output to a list with the pis name
    #call the command that outputs to the mac's terminal

parser = ap.ArgumentParser(description="Commands for the pi-cluster.")

# exclusive options
group = parser.add_mutually_exclusive_group()
#parser.add_argument('--nargs', nargs='+')
group.add_argument("-r", "--reboot", help="Reboots the cluster.", nargs="+")
group.add_argument("-s", "--shutdown", help="Shutdown the cluster.", 
    action="store_true")
group.add_argument("--rebootpi", help="Reboots a single pi.")
group.add_argument("--shutdownpi", help="Shutdown a single pi.")

args = parser.parse_args()

#if args.reboot:
    #reboot
#elif args.shutdown:
    #shutdown
for _, value in args._get_kwargs():
    pi_outputs.append(value)
#    if value is not None:
#        print(value)
#        pi_outputs.append(value)

# replace print statements with function calls for each pi
if "0" in pi_outputs[0]:
    print("found zero")
if "1" in pi_outputs[0]:
    print("found one")
if "2" in pi_outputs[0]:
    print("found two")
if "3" in pi_outputs[0]:
    print("found three")
