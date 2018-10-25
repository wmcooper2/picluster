#!/usr/bin/env python3
"""Commands for controlling the pi-cluster through ssh."""

#stand lib
import subprocess

def reboot(pi):
    """Reboot pi. Returns None."""
    command = "ssh {0} 'sudo reboot'".format(pi)
    subprocess.Popen(command, shell=True)
    print("Rebooting {0}".format(pi))

def cluster_reboot(cluster):
    """Reboot the whole cluster. Returns None."""
    map(reboot, cluster)

def ssh(pi):
    """SSH into a pi. Returns None."""
    command = "ssh {0}".format(pi)
    subprocess.Popen(command, shell=True)

def shutdown(pi):
    """Shutsdown a pi. Returns None."""
    command = "ssh {0} 'sudo shutdown -h now'".format(pi)
    subprocess.Popen(command, shell=True)
    print("Shutting down {0}".format(pi))

def cluster_shutdown():
    """Shuts down the whole cluster. Returns None."""
    map(shutdown, cluster)


if __name__ == "__main__":
    pi0 = ""
    pi1 = ""
    pi2 = ""
    pi3 = ""
#    cluster = [pi0, pi1, pi2, pi3]
#    cluster_reboot(cluster)
#    reboot(cluster[0])
    shutdown(cluster[0])

