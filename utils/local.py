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

__all__ = ["localhost"]


class localhost:

    def __init__(self):
        """
        the localhost does not even need any addresses passed. It is static.
        """
        self.__ip = "127.0.0.1"
        self.__hostname = "localhost"

    @property
    def ipAddress(self, iface=None):
        """
        :return: A dictionary of all the ip addresses on the various interface of the localhost
        """
        if iface is None:
            command = "ipconfig" if sys.platform.lower() == "windows" else "ifconfig"
        else:
            command = "ipconfig " + iface if sys.platform.lower() == "windows" else "ifconfig " + iface

        addresses = re.findall(r"addr:\d+\.\d+\.\d+\.\d+", os.popen(command).read(-1))

        if len(addresses) == 3:
            return {
                "local": addresses[0][5:],
                "wifi": addresses[2][5:],
                "other": addresses[1][5:]
            }
        elif len(addresses) == 4:
            return {
                "modem/wired": addresses[0][5:],
                "local": addresses[1][5:],
                "wifi": addresses[3][5:],
                "other": addresses[2][5:]
            }
        try:
            return addresses[0][5:]
        except IndexError:
            return NotImplemented
