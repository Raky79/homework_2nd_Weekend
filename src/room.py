class Room: 
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.songs = []
        self.guests = []
    
    def add_room(self, room): 
        self.rooms.append(room)

    def add_song(self, song): 
        self.songs.append(song)

    def add_song_to_room(self, song):
        self.rooms.append(song)

    
    def add_guest(self, guest): 
        self.guests.append(guest)

    def check_in(self, guest):
        self.guests.update(guest)
    

    
    # def check_in_guest(self, guest, room):
    #     self.room.rooms

    def check_out_guest(self, guest):
        self.guests.remove(guest)
    
  
       