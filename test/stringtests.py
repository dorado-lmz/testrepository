__author__ = 'lmz'

import unittest

class StringTest(unittest.TestCase):
  def setUp(self):
  	self.fixture="asdf"
  def testUpper(self):
    print(self.fixture)
    self.assertEquals("foo".upper(),'FOO')
  def testJoin(self):
    self.assertEquals('f'.join('oo'), 'fo', 'join has problem')
  def test_assert_raises(self):
     self.assertRaises(ValueError, raises_error, 'a', b='c')

if __name__ == '__main__':
  unittest.main()


