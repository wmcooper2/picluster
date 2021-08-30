_This is an old project and I do not intend to work on it aggressively anymore.
I may take it up again in the future, but likely it will be replaced with something better._

# Pi cluster controls

## Purpose
* Control a small cluster of raspberry pi nodes remotely from my macbook to perform concurrent work.
* To control multiple nodes to perform tasks on many (>40GB, >600,000 files) texts concurrently.
* To have a separate cluster that I can send the grunt work to, reducing wear on my Macbook.

## Setup
1. Make a file called `pi_ipaddress.txt` and put in your pi's IP addresses, one on each line like this;  
```bash
192.168.0.101
192.168.0.102
192.168.0.103
192.168.0.104
```

## Operation
### Simple, routine controls
* For routine commands use the "simple.py" module
* From the command line, run `python3 simple.py -h` for help.
* Node wlan0 ip addresses are kept in a separate module 

### Custom controls, (sudo level, be careful)
* For sending custom commands not routine, use the "custom.py" module

### To do
* Give a timeout to the commands
* Tests need more thought.
* Make sure the raspberry pis are setup with a clean install (using default login).

### What I learned
* How to use SSH to communicate with remote machines.
* How to set up password-less access through SSH.
* How to write scripts using the "argparse" library to make controlling nodes easy from the command line.
* How to assemble a mini cluster computer of 5-Raspberry Pi 3's.
