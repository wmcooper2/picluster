# Pi cluster controls

## Purpose
Control a small cluster of raspberry pi nodes remotely from my macbook to perform concurrent work.

## Setup
1. Make a file called `src/pi_ipaddress.py` and put in your pi's IP addresses, one on each line like this;  
```bash
pi1="192.168.0.101"
pi2="192.168.0.102"
pi3="192.168.0.103"
pi4="192.168.0.104"
```


## Operation

### Simple, routine controls
* For routine commands use the "simple.py" module
* From the command line, run `python3 simple.py -h` for help.
* Node wlan0 ip addresses are kept in a separate module 
  * to keep my personal info off of github

### Custom controls, (sudo level, be careful)
* For sending custom commands not routine, use the "custom.py" module
_project not finished..._

### To do
* Give a timeout to the commands
* Tests need more thought.
* Would like to get device type on network scan, if possible.
* Make sure the raspberry pis are setup with a clean install (using default login).
* Connect to pi via ethernet and check the setup to make sure `scan.py` is working right.

