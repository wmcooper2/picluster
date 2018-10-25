#!/usr/bin/env python3
"""Commands for controlling the pi-cluster through ssh."""

#stand lib
import subprocess


def reboot(pi):
    """Reboot pi. Returns None."""
    command = "ssh {0} && sudo reboot".format(pi)
    subprocess.open(command)
    print("Rebooting {0}".format(pi))

def cluster_reboot():
    """Reboot the whole cluster. Returns None."""
    map(reboot, cluster)

pi0 = ""
pi1 = ""
pi2 = ""
pi3 = ""

cluster = [pi0, pi1, pi2, pi3]



