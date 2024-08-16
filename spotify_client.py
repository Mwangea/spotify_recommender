import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                            client_secret=CLIENT_SECRET,
                                                            redirect_uri=REDIRECT_URI,
                                                            scope="user-top-read user-read-recently-played"))

    def get_user_top_tracks(self, limit=50):
        return self.sp.current_user_top_tracks(limit=limit)

    def get_user_top_artists(self, limit=50):
        return self.sp.current_user_top_artists(limit=limit)

    def get_track_features(self, track_id):
        return self.sp.audio_features([track_id])[0]

    def get_recommendations(self, seed_tracks, seed_artists, limit=20):
        return self.sp.recommendations(seed_tracks=seed_tracks, seed_artists=seed_artists, limit=limit)

    def get_genre_recommendations(self, genres, limit=20):
        return self.sp.recommendations(seed_genres=genres, limit=limit)