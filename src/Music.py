class Song:

    def __init__(self, art, alb, y, name):
        self.__artist = art
        self.__album = alb
        self.__year = y
        self.__name = name


    @property
    def name(self):
        return self.__name

    @property
    def art(self):
        return self.__artist

    @property
    def alb(self):
        return self.__album

    @property
    def y(self):
        return self.__year

    def __str__(self):
        return "{} {} {} {}".format(self.__artist,self.__album, self.__year, self.__name)



class Playlist:

    def __init__(self, s):
        self.__songs = s

    @property
    def songs(self):
        return self.__songs


    def load_songs(self):
        with open('albums.txt') as f:
            for i in f.readlines():
                l = i.split('\t')
                #print(l)
                #print(type(l))
                a = Song(l[0],l[1],l[2],l[3])
                # print(a)
                self.__songs.append(a)
        return self.__songs


    def __repr__(self):
        s = ''
        for i in self.__songs:
            s += i.art + " " + i.alb + " " + i.y + " " + i.name
        return s



class Player:

    def __init__(self, pl):
        self.__playlist = pl
        self.__current_song = self.__playlist.songs[0]
        self.__status = False

    @property
    def playlist(self):
        return self.__playlist


    def __repr__(self):
        return "{}".format(self.__status)


    def get_current_song(self):
        return self.__current_song

    def play(self):
        self.__status = True
        print(self.__current_song)
        return self.__status

    def stop(self):
        self.__status = False
        print(self.__current_song)
        return self.__status

    def select_song(self, x):
        self.__current_song = self.__playlist.songs[x]
        return self.__current_song

    def previous_song(self):
        a = self.__playlist.songs.index(self.__current_song) - 1
        return self.__playlist.songs[a]



################################################

# song1 = Song('Eric Clapton', "Journeyman", '1969', 'Old Love')
# plist1 = Playlist([song1,song2,song3])
# print(plist1)
plist3 = Playlist([])
plist3.load_songs()
pl1 = Player(plist3)
print(pl1)
a = pl1.get_current_song()
print(a)
b = pl1.play()
print(b)
c = pl1.stop()
print(c)
d = pl1.select_song(10)
print(d)
e = pl1.previous_song()
print(e)