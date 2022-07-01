import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Sam", 100, "Yesterday")

    def test_guest_has_been_set_up_properly(self):    
        self.assertEqual("Sam", self.guest1.name)
        self.assertEqual(100, self.guest1.wallet)
        self.assertEqual("Yesterday", self.guest1.fav_song)