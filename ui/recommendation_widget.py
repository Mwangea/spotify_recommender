from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import requests  # Add this import

class RecommendationWidget(QWidget):
    def __init__(self, track):
        super().__init__()
        self.track = track
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Album cover
        album_cover = QLabel()
        pixmap = QPixmap()
        try:
           response = requests.get(self.track['album']['images'][0]['url'])
           response.raise_for_status()
           pixmap.loadFromData(response.content)
        except requests.RequestException as e:
           print(f"Error loading album cover: {e}")
        album_cover.setPixmap(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(album_cover)

        # Track info
        info_layout = QVBoxLayout()
        track_name = QLabel(self.track['name'])
        track_name.setObjectName("trackName")
        artists = QLabel(', '.join([artist['name'] for artist in self.track['artists']]))
        artists.setObjectName("artistName")
        info_layout.addWidget(track_name)
        info_layout.addWidget(artists)
        layout.addLayout(info_layout)

        layout.addStretch()