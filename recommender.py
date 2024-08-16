from config import NUM_RECOMMENDATIONS

class Recommender:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client
        
    def get_recommendations(self, user_profile):
        seed_tracks = [track['id'] for track in user_profile.top_tracks['items'][:2]]
        seed_artists = [artist['id'] for artist in user_profile.top_artists['items'][:3]]
        
        
        recommendations = self.spotify_client.get_recommendations(seed_tracks, seed_artists, limit=NUM_RECOMMENDATIONS)
        return recommendations['tracks']