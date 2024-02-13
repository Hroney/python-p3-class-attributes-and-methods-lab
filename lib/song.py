class Song:

    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
        
    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            cls.artist_count[artist] = cls.artist_count.get(artist) + 1
        else:
            cls.artists.add(artist)
            cls.artist_count.update({artist: 1})

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genres:
            cls.genre_count[genre] = cls.genre_count.get(genre) + 1
        else:
            cls.genres.add(genre)
            cls.genre_count.update({genre: 1})



    pass
