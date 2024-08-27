class Playlist:
    def __init__ (self, playlist = []):
        self.playlist = playlist

    def load_playlist(self):
        file = open('glblcd_MP3\playlist.txt','r')
        read = file.readlines()
        for line in read:
            self.playlist.append(line.strip())

    def display_playlist(self):
        for song in self.playlist: 
            print(song)

    def add_mp3(self,song):
        self.playlist.append(song)

my_playlist=Playlist()
my_playlist.load_playlist()
# print(my_playlist.display_playlist())
new=my_playlist.add_mp3("Love you Lord")
my_playlist.display_playlist()
        
