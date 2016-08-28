__author__ = 'lmz'

import unittest

class ListTest(unittest.TestCase):
  def runTest(self):
    print "sfsdf"

def suite():
  suite = unittest.TestSuite()
  testcase = ListTest()
  suite.addTest(testcase)
  return suite

if __name__ == '__main__':
  suite = suite()
  runner = unittest.TextTestRunner()
  runner.run(suite)



