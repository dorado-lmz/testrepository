import unittest
import mock

import client

class ClientTest(unittest.TestCase):
  def test_success_request(self):
    success_send = mock.Mock(return_value='200')
    client.send_request = success_send
    self.assertEquals(client.visit_baidu(), '200')

  def test_fail_request(self):
    fail_send = mock.Mock(return_value='404')
    client.send_request = fail_send
    self.assertEquals(client.visit_baidu(), '404')

if __name__ == '__main__':
  unittest.main()


