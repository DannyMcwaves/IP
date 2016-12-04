"""
this local file configuration is mainly for the system that checks the features
of this particular system. Aside from the localhost name it check for the address on the
various interfaces if any.

Also contains functions that returns the current state of the machine. Among others I am yet
to figure out for myself.
"""

import sys
import re
import os


class localhost:

    def __init__(iface=None):
        if iface is None:
            command = "ipconfig" if sys.platform.lower() == "windows" else "ifconfig"
        else:
            command = "ipconfig " + iface if sys.platform.lower() == "windows" else "ifconfig " + iface
        addrs = re.findall(r"addr:\d+\.\d+\.\d+\.\d+", os.popen(command).read(-1))

        if len(addrs) == 3:
            return {
                "local": addrs[0][5:],
                "wifi": addrs[2][5:],
                "other": addrs[1][5:]
            }
        elif len(addrs) == 4:
            return {
                "modem/wired": addrs[0][5:],
                "local": addrs[1][5:],
                "wifi": addrs[3][5:],
                "other": addrs[2][5:]
            }
        try:
            return addrs[0][5:]
        except IndexError:
            return NotImplemented
