#!/usr/bin/env python3
"""Commands to control the pi-cluster."""

#stand lib
import argparse as ap

#custom
from pi_ipaddresses import *

parser = argparse.ArgumentParser(description="Commands for the pi-cluster.")
#parser.add_argument("-r", "--reboot", help="Reboots the cluster." )
#parser.add_argument("-s", "--shutdown", help="Shutdown the cluster.")


# exclusive options
group = parser.add_mutually_exclusive_group()
group.add_argument("-r", "--reboot", help="Reboots the cluster.", 
    action="store_true")
group.add_argument("-s", "--shutdown", help="Shutdown the cluster.", 
    action="store_true")
group.add_argument("--rebootpi", help="Reboots a single pi.")
group.add_argument("--shutdownpi", help="Shutdown a single pi.")

#group.add_argument()
#group.add_argument()


args.parser.parse_args()


if args.reboot:
    #reboot
elif args.shutdown:
    #shutdown

