from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from .recommendation_widget import RecommendationWidget
from user_profile import UserProfile
import os

class MainWindow(QMainWindow):
    def __init__(self, spotify_client, recommender, breakout_recommender):
        super().__init__()
        self.spotify_client = spotify_client
        self.recommender = recommender
        self.breakout_recommender = breakout_recommender
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Spotify Recommender")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("path_to_your_icon.png"))  # Add your own icon

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Get Recommendations button
        self.get_recommendations_button = QPushButton("Get Recommendations")
        self.get_recommendations_button.clicked.connect(self.get_recommendations)
        layout.addWidget(self.get_recommendations_button)

        # Recommendations area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.recommendations_widget = QWidget()
        self.recommendations_layout = QVBoxLayout(self.recommendations_widget)
        scroll_area.setWidget(self.recommendations_widget)
        layout.addWidget(scroll_area)

        self.load_stylesheet()

    def load_stylesheet(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        style_path = os.path.join(current_dir, "resources", "styles.qss")
        with open(style_path, "r") as f:
            self.setStyleSheet(f.read())

    def get_recommendations(self):
        user_profile = UserProfile(self.spotify_client)
        user_profile.build_profile()

        regular_recommendations = self.recommender.get_recommendations(user_profile)
        breakout_recommendations = self.breakout_recommender.get_breakout_recommendations(user_profile)

        self.display_recommendations(regular_recommendations, "Regular Recommendations")
        self.display_recommendations(breakout_recommendations, "Breakout Recommendations")

    def display_recommendations(self, recommendations, title):
        section_label = QLabel(title)
        section_label.setObjectName("sectionLabel")
        self.recommendations_layout.addWidget(section_label)

        for track in recommendations:
          recommendation_widget = RecommendationWidget(track)
          self.recommendations_layout.addWidget(recommendation_widget)

        self.recommendations_layout.addStretch()