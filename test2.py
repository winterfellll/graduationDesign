class test():
    def __init__(self):
        print('init')

    def go(self):
        print('go')


import unittest


class se(unittest.TestCase, test):

    def test_01(self):
        self.go()
