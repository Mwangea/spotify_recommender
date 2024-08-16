import random
from config import NUM_BREAKOUT_RECOMMENDATIONS


class BreakoutRecommender:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client
        
    def get_breakout_recommendations(self, user_profile):
        all_genres = self._get_all_genres()
        new_genres = list(set(all_genres) - set(user_profile.favorite_genres))
        selected_genres = random.sample(new_genres, min(3, len(new_genres)))
        
        
        recommendations = self.spotify_client.get_genre_recommendations(selected_genres, limit=NUM_BREAKOUT_RECOMMENDATIONS)
        return recommendations['tracks']
    
    
    def _get_all_genres(self):
        # This is a simplified list. In a real application, you'd fetch this from Spotify's API
        return ['pop', 'rock', 'hip-hop', 'jazz', 'classical', 'electronic', 'country', 'r-n-b', 'indie', 'metal']