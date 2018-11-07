#!/usr/bin/env python3
"""Example from the python docs online to show adding args.
    https://stackoverflow.com/questions/15753701/argparse-option-for-passing-a-list-as-option
"""

import argparse

parser = argparse.ArgumentParser()
#parser.add_argument('--default')
#parser.add_argument('--list-type', type=list)
#parser.add_argument('--list-type-nargs', type=list, nargs='+')
parser.add_argument('--nargs', nargs='+')
#parser.add_argument('--nargs-int-type', nargs='+', type=int)
#parser.add_argument('--append-action', action='append')
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        print(value)
        
