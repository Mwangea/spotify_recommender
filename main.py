import sys
from PyQt5.QtWidgets import QApplication
from spotify_client import SpotifyClient
from recommender import Recommender
from breakout_recommender import BreakoutRecommender
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    spotify_client = SpotifyClient()
    recommender = Recommender(spotify_client)
    breakout_recommender = BreakoutRecommender(spotify_client)

    main_window = MainWindow(spotify_client, recommender, breakout_recommender)
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()