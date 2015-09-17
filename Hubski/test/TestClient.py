import unittest
from Hubski.Hubski import Hubski, Publication
from pprint import pprint


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Hubski()
        self.pub = self.client.get_pub(1)

    def tearDown(self):
        pass

    def test_user_get(self):
        #raise NotImplementedError
        pass

    def test_pub_get(self):
        self.assertEqual(self.pub.tag, "hubski")

    def test_vote_sort(self):
        self.assertEqual(self.pub.sortByVote()[0]['num'], 0)

if __name__ == '__main__':
    unittest.main()