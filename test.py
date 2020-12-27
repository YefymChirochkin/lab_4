import unittest

from wchain import WChain

path = 'test_files/'


class WChainTest(unittest.TestCase):

    def test_chain1(self):
        w = WChain(path + "wchain1.in")
        self.assertEqual(6, w.count_chains())

    def test_chain2(self):
        w = WChain(path + "wchain2.in")
        self.assertEqual(4, w.count_chains())

    def test_chain3(self):
        w = WChain(path + "wchain3.in")
        self.assertEqual(4, w.count_chains())

    def test_chain4(self):
        w = WChain(path + "wchain4.in")
        self.assertEqual(1, w.count_chains())


if __name__ == '__main__':
    unittest.main()