import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Codeclan Caraoke")
        self.room.songs = [ 
        {
            "name" : "1979",
            "artist" : "The Smashing Pumpkins",
            "genre" : "Pop Rock"
        },
        {
            "name" : "The Trooper",
            "artist" : "Iron Maiden",
            "genre" : "Metal"
        },
        {
            "name" : "Baba O'riley",
            "artist" : "The Who",
            "genre" : "Rock"
        }
        ], 
        self.room.rooms = [
        {
        "room_1" : "Metal Valhalla",
        "room_2" : "90's Party",
        "room_3" : "So Retro, so Good"
        }
        ], 
        self.room.guests = [
        {
        "name" : "Billy",
        "age" : 29
        }, 
        {
        "name" : "Travis",
        "age" : 17
        }, 
        {
         "name" : "Robert",
         "age" : 32   
        }
        ]
    


    def test_room_has_name(self):
        self.assertEqual("Codeclan Caraoke", self.room.name)

    def test_room_has_songs(self):
        result = self.room.songs
        self.assertEqual(result,self.room.songs)
    
    def test_room_has_rooms(self):
        result = self.room.rooms
        self.assertEqual(result,self.room.rooms)
    
    def test_room_has_guests(self):
        result = self.room.guests
        self.assertEqual(result,self.room.guests)
    
    def add_songs_to_rooms(self):
        song = self.room.songs[1]
        room = self.room.rooms[1]
        self.room.add_song_to_room(song[room])
        self.assertEqual(song[room], self.room.rooms)


        # def test_library_can_add_book(self):
        # # AAA
        # # Arrange - do your setup
        # book = Book("The Hobbit", "J R R Tolkien", "Fantasy")
        # # Act
        # self.library.add_book(book)
        # # Assert
        # self.assertEqual([book], self.library.books)

        
    
    # def test_room_has_guests(self): 
    #     self.assertEqual([], self.room.guests)

    # def test_room_can_add_rooms(self): 
    #     room_1 = Room("Metal Valhalla")
    #     room_2 = Room("90's Party")
    #     room_3 = Room("So Retro, so Good")
    #     self.room.add_room(room_1)
    #     self.room.add_room(room_2)
    #     self.room.add_room(room_3)
    #     self.assertEqual([room_1, room_2, room_3], self.room.rooms)


    # def test_room_can_add_songs(self):
    #     nineteen_seventy_nine = Song("1979", "The Smashing Pumpkins", "Pop Rock")
    #     the_trooper = Song("The Trooper", "Iron Maiden", "Metal")
    #     baba_o_riley = Song("Baba O'riley", "The Who", "Rock")
    #     self.room.add_song(nineteen_seventy_nine)
    #     self.room.add_song(the_trooper)
    #     self.room.add_song(baba_o_riley)
    #     self.assertEqual([nineteen_seventy_nine, the_trooper, baba_o_riley], self.room.songs)
    
    # def test_room_can_add_guest(self):
    #     guest_1 = Guest("Billy", 29)
    #     guest_2 = Guest("Travis", 17)
    #     guest_3 = Guest("Robert", 32) 
    #     self.room.add_guest(guest_1)
    #     self.room.add_guest(guest_2)
    #     self.room.add_guest(guest_3)
    #     self.assertEqual([guest_1, guest_2, guest_3], self.room.guests)
    
    # def test_guest_check_in_rooms(self):
        
    #     self.guest_1 = Guest("Billy", 29)
    #     self.room_1 = Room("Metal Valhalla")
    #     self.room_1.check_in(self.guest_1)
    #     self.assertEqual({self.room_1[self.guest_1]}, self.room.guests)
        
        
        # self.room_2.add_guest(self.guest_2)
        # self.room_3.add_guest(self.guest_3)  
        # self.assertEqual([(self.room_1, self.guest_1), (self.room_2, self.guest_2), (self.room_3, self.guest_3)])   

        # self.assertEqual([room_1(guest_1)])
     
 



    #     guest_1 = Guest("Billy", 29)
    #     guest_2 = Guest("Travis", 17)
    #     guest_3 = Guest("Robert", 32)
    #     # room_1 = Room("Metal Valhalla")
    #     # room_2 = Room("90's Party")
    #     # room_3 = Room("So Retro, so Good")
    #     self.room.check_in_guest(guest_1)
    #     self.room.check_in_guest(guest_2)
    #     self.room.check_in_guest(guest_3)
    # #     guest_1 = Guest("Billy", 29)
    # #     guest_2 = Guest("Travis", 17)
    # #     guest_3 = Guest("Robert", 32)
    # #     room_1 = Room("Metal Valhalla")
    # #     room_2 = Room("90's Party")
    # #     room_3 = Room("So Retro, so Good")
    #     self.assertEqual(self.room.check_in_guest(self.guest_1)) 
      
        


        
    
 

        
    

    
