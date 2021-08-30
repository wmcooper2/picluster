"""Simple, routine commands to control the pi-cluster."""

# stand lib
import argparse as ap
from pathlib import Path
from pprint import pprint
import subprocess
from typing import Any, List

# custom
from pi_ipaddresses import *
from util import addresses


pi_outputs: list = []                        # holds stdout from pis
valid_args: list = ["1", "2", "3", "4"]
given_args: list = []                        # holds args from command line
message: list = ["Please choose any combo of the nodes (1 2 3 or 4).",
                 "\n", "You can choose a maximum of four nodes at a time.",
                 "\n", "Leave blank to choose all.",
                 "\n"]


def not_none(args: list) -> bool:
    """Checks that args for a flag are not None. Returns Boolean."""
    if args[1] is not None:
        return True
    else:
        return False


def clear_terminal() -> None:
    """Clears the terminal window. Returns None."""
    subprocess.run(["clear"])
    return None


def show_outputs() -> None:
    """Shows the outputs of the pis. Returns None."""
    for output in pi_outputs:
        print(str(pi_outputs.index(output)), "::", output)
    return None


def format_pi_name(name: str) -> str:
    """Formats the pi name. Returns String."""
    piname = "pi@"+name
    return piname


def format_cmd(a: str, b: str) -> str:
    """Formats the command. Returns String."""
    return "ssh "+a+" '"+b+"'"


def print_kwargs() -> None:
    """Displays kwargs given at command line. Returns None."""
    for _, value in args._get_kwargs():
        given_args.append(value)
        print(_, "::", value)
    return None


def print_pi_outputs() -> None:
    """Displays contents of pi_outputs. Returns None."""
    for out in pi_outputs:
        print(out.stdout)
    return None


def run_cmd(cmd: str) -> str:
    """Runs cmd in a subprocess. Returns stdout String."""
    return subprocess.run(cmd, encoding="utf-8", shell=True, stdout=subprocess.PIPE).stdout


def _reboot(pi: str) -> None:
    """Reboots all the nodes in cluster. Returns None."""
    name = format_pi_name(pi)
    cmd = format_cmd(name, "sudo reboot")
    run_cmd(cmd)
    return None


def _shutdown(pi: str) -> None:
    """Shutsdown all the nodes in cluster. Returns None."""
    name = format_pi_name(pi)
    cmd = format_cmd(name, "sudo shutdown -h now")
    run_cmd(cmd)
    return None


def _name(pi: str) -> None:
    """Displays the name of the machine. Returns None."""
    name = format_pi_name(pi)
    cmd = format_cmd(name, "hostname")
    result = run_cmd(cmd)
    print(result.strip())
    return None


def _ipaddr(pi: str) -> None:
    """Displays the wlan0 ipaddress of the node. Returns None."""
    name = format_pi_name(pi)
    cmd = format_cmd(name, "hostname -I")
    result = run_cmd(cmd)
    print("pi{}".format(pi), result.strip())
    return None


def _mount(pi: str) -> None:
    """Mount the usb drives to the nodes. Returns None."""
    name = format_pi_name(pi)
    cmd = format_cmd(name, "sudo mount /dev/sda1 /mnt/usb")
    run_cmd(cmd)
    print("{}: mounted {} at {}".format(name, "/dev/sda1", "/mnt/usb"))
    return None


def _umount(pi: str) -> None:
    """Unmounts the usb drives from the nodes. Returns None."""
    name = format_pi_name(pi)
    cmd = format_cmd(name, "sudo umount /dev/sda1 /mnt/usb")
    run_cmd(cmd)
    print("{}: unmounted {} from {}".format(name, "/dev/sda1", "/mnt/usb"))
    return None


def _list(pi: str, args: Any) -> None:
    """List the dir names of a node's /mnt/usb."""
    name = format_pi_name(pi)
    cmd = None
    if args.verbose:
        cmd = format_cmd(name, "ls -al /mnt/usb/")
    else:
        cmd = format_cmd(name, "ls /mnt/usb/")
    print(name)
    print(run_cmd(cmd).strip())
    print("\n")
    return None


def apply_to_each(f: Any, args: list) -> None:
    """Runs each function on arg in args. Returns None."""
    for arg in args:
        f(arg)
    return None


def run_simple(args: Any) -> None:
    """Runs a simple command. Returns None."""
    if args.reboot:
        apply_to_each(_reboot, cluster)
    elif args.shutdown:
        apply_to_each(_shutdown, cluster)
    elif args.name:
        apply_to_each(_name, cluster)
    elif args.ipaddr:
        apply_to_each(_ipaddr, cluster)
    elif args.mount:
        apply_to_each(_mount, cluster)
    elif args.umount:
        apply_to_each(_umount, cluster)
    elif args.list:
        apply_to_each(_list, cluster)
    return None


if __name__ == "__main__":

    cluster: List = addresses()

    parser = ap.ArgumentParser(description="Commands for the pi-cluster.")
    parser.add_argument("-v", "--verbose", help="Be verbose.", action="store_true")

    # simple, common commands
    simple = parser.add_mutually_exclusive_group()
    simple.add_argument("-r", "--reboot",   help="Reboots the cluster.",        nargs="?")
    simple.add_argument("-s", "--shutdown", help="Shuts down the cluster.",     nargs="?", const=valid_args)
    simple.add_argument("-n", "--name",     help="Displays name of the node.",  nargs="?", const=valid_args)
    simple.add_argument("-i", "--ipaddr",   help="Displays node's ipaddress.",  nargs="?", const=valid_args)
    simple.add_argument("-m", "--mount",    help="Mounts the usb drives.",      nargs="?", const=valid_args)
    simple.add_argument("-u", "--umount",   help="Unmounts the usb drives.",    nargs="?", const=valid_args)
    simple.add_argument("-l", "--list",     help="List dirs in /mnt/usb",       nargs="?", const=valid_args)
    args = parser.parse_args()
    clear_terminal()
    print()
    a = list(filter(not_none, args._get_kwargs()))

    run_simple(args)

    # End program
    parser.exit(status=0, message="Finished.\n")
