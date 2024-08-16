class UserProfile:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client
        self.top_tracks = []
        self.top_artists = []
        self.favorite_genres = set()

    def build_profile(self):
        self.top_tracks = self.spotify_client.get_user_top_tracks()
        self.top_artists = self.spotify_client.get_user_top_artists()
        self._extract_favorite_genres()

    def _extract_favorite_genres(self):
        for artist in self.top_artists['items']:
            self.favorite_genres.update(artist['genres'])