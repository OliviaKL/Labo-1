# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        return self.assertEqual (utils.fact(0), 1)
    
    def test_roots(self):
        return self.assertEqual (utils.roots(0, 1, 2), 1)
    
    def test_integrate(self):
        return self.assertEqual (utils.integrate(0, 1, 2), 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
