import unittest

from src.song import Song  


class TestSong(unittest.TestCase):
    def setUp(self):    
        self.song = Song("1979", "The Smashing Pumpkins", "Pop Rock")
    
    def test_song_has_name(self):
        self.assertEqual("1979", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("The Smashing Pumpkins", self.song.artist)
    
    def test_song_has_genre(self):
        self.assertEqual("Pop Rock", self.song.genre)