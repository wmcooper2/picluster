#std lib
import subprocess
import sys
from typing import List, Text


def ask_if_ips_are_known() -> bool:
    answer = input("Do you know your Raspberry Pi IP addresses? [y|n] ").lower()
    while answer not in "yn":
        answer = input("Do you know your Raspberry Pi IP addresses? [y|n] ").lower()
    if answer == "y":
        return True
    else:
        return False


def ask_which_network() -> Text:
    answer = input("Wifi [w], ethernet [e], or quit [q]? ").lower()
    while answer not in "weq":
        answer = input("Wifi [w], ethernet [e], or quit [q]? ").lower()
    return answer 


def ethernet_ip() -> Text:
    result = subprocess.run(["ipconfig", "getifaddr", "en1"], capture_output=True)
    return result.stdout.strip().decode("ascii")


def is_mac() -> bool:
    if sys.platform == "darwin":
        return True


def addresses() -> List[Text]:
    with open("pi_addresses.txt", "r") as f:
        addresses = f.read()
    return addresses


def ping(network, host):
    result = subprocess.run(["ping", "-c", "1", f"{network}{str(host)}"], capture_output=True)
    if b"64 bytes" in result.stdout:
        print(f"Something here: {network}{host}")
    else:
        print("No:", host)


def simple_scan() -> None:
    for host in range(2, 255): #host range
        print("Host:", host)
        ping(network, host)


def wifi_ip() -> Text:
    result = subprocess.run(["ipconfig", "getifaddr", "en0"], capture_output=True)
    return result.stdout.strip().decode("ascii")
