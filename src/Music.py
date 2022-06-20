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
        self.__is_valid = False
        self.__playlist = pl
        self.__is_valid = True


    @property
    def playlist(self):
        return self.__playlist

    @property
    def is_valid(self):
        return self.__is_valid

    def __str__(self):
        return "{}".format(self.__playlist)


    def play(self,a):
        for x in self.__playlist.name:
            print(a)



    # def stop(self, a):
    #     pass
    #
    # def previous_song(self,a):
    #     pass
    #
    # def show_current_song(self):
    #     pass


################################################

song1 = Song('Eric Clapton', "Journeyman", '1969', 'Old Love')
# print(song1)
song2 = Song('Eric Clapton', "JJJ", '1990', 'OOO')
song3 = Song('Eric Clapton', "KKK", '2000', '111')
# plist1 = Playlist([song1,song2,song3])
# plist2 = Playlist([song2,song3])
# print(plist1)
plist3 = Playlist([])
plist3.load_songs()
# plist1.load_songs()
# print(plist3)

pl1 = Player(plist3)
# print(pl1)
pl1.play(4)
# print(pl1)

