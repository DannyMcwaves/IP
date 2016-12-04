"""
this is the main module that provides most of the functionality I am trying to implement
in this package
"""

import ipaddress
from ip import Resolve
from ip import localhost


class IP:

    """
    the main purpose of the IP is for manipulating ip addresses, masking subnets, checking for the attributes
    on IPS. the subclasses they belong or the hostmask.
    """

    def __init__(self, address: str, mask: int="32"):
        """
        :param address: The IP address
        :param mask: this is the mask it should take for the number of hosts that you are planning to access
                      the mask can be a valid host mask or a valid net_mask or a num_digit slash.
                      host mask starts with 0 and contain either 0's and 255's
                      net masks start with 255 and contain either 0's and 255's
        """
        address = Resolve(address).address
        self.__mask = mask
        self.address = address + "/" + str(mask)
        self.mask_addr = ipaddress.IPv4Network(self.address, strict=False)

    @property
    def mask(self):
        return self.mask

    @mask.setter
    def mask(self, value: int):
        self.mask = value
        self.address = self.address.split("/")[0] + "/" + str(value)
        self.mask_addr = ipaddress.IPv4Network(self.address, strict=False)

    @property
    def hostmask(self):
        return self.mask_addr.hostmask

    @property
    def netmask(self):
        return self.mask_addr.netmask

    @property
    def network_address(self):
        return self.mask_addr.network_address

    @property
    def number_of_hosts(self):
        return self.mask_addr.num_addresses

    @property
    def hosts(self):
        return self.mask_addr.hosts()

    @property
    def subnets(self):
        return self.mask_addr.subnets()


if __name__ == '__main__':
    # from pprint import pprint
    ip = IP("gstatic.com")
    print(ip.address)
    m = ip.mask(24)
    print(m.address)
    print(m.number_of_hosts)
    print([x for x in m.subnets])
    for i in m.hosts:
        print(i)
