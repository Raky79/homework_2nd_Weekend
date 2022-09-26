import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song



class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Amy", 40)

    def test_guest_has_name(self):
        self.assertEqual("Amy", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(40, self.guest.age)
    