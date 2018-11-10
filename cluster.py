#!/usr/bin/env python3
"""Commands to control the pi-cluster."""

#To do:
    # set up passing a search string to the nodes
    # set up a script in each node that saves results of a search on the local node and then another command to check that the processes are finished, then another to retrieve the results?

#stand lib
import argparse as ap
import subprocess
from time import sleep

#custom
from pi_ipaddresses import *

cluster     = [pi1, pi2, pi3, pi4]      # ip addresses
pi_outputs  = []                        # holds stdout from pis
valid_args  = ["1", "2", "3", "4"]
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

def format_pi_name(string):
    """Formats the pi name. Returns String."""
    piname = "pi@"+string
    return piname

def format_cmd(str1, str2):
    """Formats the command. Returns String."""
    return "ssh "+str1+" '"+str2+"'"

def print_kwargs():
    """Displays kwargs given at command line. Returns None."""
    for _, value in args._get_kwargs():
        given_args.append(value)
        print(_, "::", value)

def print_pi_outputs():
    """Displays contents of pi_outputs. Returns None."""
    [print(out.stdout) for out in pi_outputs]

def run_cmd(cmd):
    """Runs cmd in a subprocess. Returns stdout String."""
    return subprocess.run(cmd, encoding="utf-8", shell=True,
                          stdout=subprocess.PIPE).stdout

def _reboot(pi):
    """Reboots all the nodes in cluster. Returns None."""
    name = format_pi_name(cluster[int(pi)-1])
    cmd = format_cmd(name, "sudo reboot")
    run_cmd(cmd)

def _shutdown(pi):
    """Shutsdown all the nodes in cluster. Returns None."""
    name = format_pi_name(cluster[int(pi)-1])
    cmd = format_cmd(name, "sudo shutdown -h now")
    run_cmd(cmd)

def _name(pi):
    """Displays the name of the machine. Returns None."""
    name = format_pi_name(cluster[int(pi)-1])
    cmd = format_cmd(name, "hostname")
    result = run_cmd(cmd)
    print(result.strip())

def _ipaddr(pi):
    """Displays the wlan0 ipaddress of the node. Returns None."""
    name = format_pi_name(cluster[int(pi)-1])
    cmd = format_cmd(name, "ip -4 address")
    result = run_cmd(cmd)
    elements = result.strip().split()
    [print(pi, "::", el) for el in elements 
        if el.startswith("192") and el.endswith("24")]

def _mount(pi):
    """Mount the usb drives to the nodes. Returns None."""
    name = format_pi_name(cluster[int(pi)-1])
    cmd = format_cmd(name, "sudo mount /dev/sda1 /mnt/usb")
    run_cmd(cmd)

def _umount(pi):
    """Unmounts the usb drives from the nodes. Returns None."""
    name = format_pi_name(cluster[int(pi)-1])
    cmd = format_cmd(name, "sudo umount /dev/sda1 /mnt/usb")
    run_cmd(cmd)

# Main
parser = ap.ArgumentParser(description="Commands for the pi-cluster.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-r", "--reboot", help="Reboots the cluster.", 
    nargs="?", const=valid_args)
group.add_argument("-s", "--shutdown", help="Shuts down the cluster.",
    nargs="?", const=valid_args)
group.add_argument("-n", "--name", help="Displays the name of the node.",
    nargs="?", const=valid_args)
group.add_argument("-i", "--ipaddr", help="Displays ipaddress of node.",
    nargs="?", const=valid_args)
group.add_argument("-m", "--mount", help="Mounts the usb drives.",
    nargs="?", const=valid_args)
group.add_argument("-u", "--umount", help="Unmounts the usb drives.",
    nargs="?", const=valid_args)

args = parser.parse_args()
clear_terminal()
print("\n")     # for nice terminal output

#if all([arg in valid_args for arg in args.name]) and len(args.name) <= 4: 
if args.reboot:
    [_reboot(arg) for arg in args.reboot]
elif args.shutdown:
    [_shutdown(arg) for arg in args.shutdown]
elif args.name:
    [_name(arg) for arg in args.name]
elif args.ipaddr:
    [_ipaddr(arg) for arg in args.ipaddr]
elif args.mount:
    [_mount(arg) for arg in args.mount]
elif args.umount:
    [_umount(arg) for arg in args.umount]
#else:
#    print("Please choose any combination of the four nodes (1 2 3 or 4).\nYou can choose a maximum of four nodes at a time.\nLeave blank to choose all.\n")

# End program
parser.exit(status=0, message="Finished.\n")
