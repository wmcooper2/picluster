#!/usr/bin/env python3
"""Test the state of the cluster."""

#stand lib
#import subprocess as s

#3rd party
#import pytest

#custom
from custom import custom_cmd as c
from custom import cluster
from pi_ipaddresses import *


def test_cluster_echo():
    for pi in cluster:
        result = c(pi, "echo yes")
#        result = s.run(["python3", "custom.py", "echo yes"])
        assert result.strip().split()[1] == "yes"
#    print(s.run(["python3", "custom.py", "-v", "hostname -I"]))


#def test_usb_mounted():
#    for pi in cluster:
#        result = c(pi, "test -d /mnt/usb")
#        assert result == None 

