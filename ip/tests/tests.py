"""
this contains at least three base classes that are used to test for the
various classes available in this package.

TESTS should be provided for Resolve, IP, and Localhost
"""


import unittest
from ip.resolve import Resolve, UnResolvedException
from ip.utils import Localhost
from ip._ip import IP


class IPTestCase(unittest.TestCase):
    """
    Test case for the Resolve package.
    """

    def test_valid_IP_Name(self):
        """
        :return: the first function to resolve if the name or the address passed to the resolve initializer is valid
        """
        tests_cases = ["127.0.0.1", "facebook.com", "www.google.com", "fruitytoes.org", "3445.097.8972.233"]
        self.assertIsInstance(Resolve(tests_cases[1]), Resolve, msg="Yes It is Instance of Resolve Class")

        # this is supposed to catch an error for function passing wrong names.
        with self.assertRaises(UnResolvedException):
            Resolve(tests_cases[-1])

        with self.assertRaises(UnResolvedException):
            Resolve(tests_cases[3])

    def test_localhost(self):

        local = Localhost()
        self.assertIsInstance(local, Localhost)

    def test_IP(self):
        _ip = IP("facebook.com")
        self.assertIsInstance(_ip, IP)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
