#!/usr/bin/env python3
"""Testing out named pipes on raspberry pi, ssh access."""

#stand lib
import subprocess

#custom
from pi_ipaddresses import *

command = "ssh pi@192.168.1.12 'ls -al'"
print("command ::", command)
#command = ["ssh", pi0, "&&", "cat", "shuryo"]
#both worked...???
#c = subprocess.Popen(command, encoding='utf-8', stdout=True, shell=True)
c = subprocess.Popen(command, encoding='utf-8', stdout=subprocess.PIPE, shell=True)

for line in c.stdout:
    print(line.strip())

#a = subprocess.run(["ssh", pi0], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#command = "ssh pi@"+pi0+ " && cat shuryo"
#command = "ssh pi@"+pi0+" && ls -al"
#command = "ssh pi@192.168.1.12"
#command = ["ssh", "-vvv", pi0]
#a = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


#a = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#a = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

#a.communicate("raspberry\n")
#a.communicate("ls")
#print(a.stdout)

#b = subprocess.run(command, shell=True, stdout=subprocess.PIPE, capture_output=True)


#c = subprocess.run(['ssh pi@192.168.1.12', '-l'], encoding='utf-8', stdout=subprocess.PIPE)
#c = subprocess.Popen(command, encoding='utf-8', stdout=subprocess.PIPE, shell=True)






#c = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE, shell=True)
#c = subprocess.run(command, encoding='utf-8', capture_output=True, shell=True)
#c.communicate(input="ls -al")
#print(c.stdout)
#for line in c.stdout.split("\n"):
#for line in c.stdout:
#    print(line)
#c.kill()
#print(c.stdout)

