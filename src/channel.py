import json
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel_id_ = self.channel["items"][0]["id"]
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = self.channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    @property
    def channel_id(self):
        self.channel_id == channel_id

    def to_json(self, file):
        data = {
            "channel_id_": self.channel["items"][0]["id"],
            "title": self.channel["items"][0]["snippet"]["title"],
            "description": self.channel["items"][0]["snippet"]["description"],
            "url": self.channel["items"][0]["snippet"]["thumbnails"]["default"]["url"],
            "subscriber_count": self.channel["items"][0]["statistics"]["subscriberCount"],
            "video_count": self.channel["items"][0]["statistics"]["videoCount"],
            "view_count": self.channel["items"][0]["statistics"]["viewCount"]
        }
        with open("moscowpython.json", "w") as file:
            json.dump(data, file)
