import json
import os
from googleapiclient.discovery import build


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

    def __str__(self):
        return f'{self.title} ({self.url})'

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

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __sub__(self, other):
        return int(other.subscriber_count) - int(self.subscriber_count)

    def __gt__(self, other):
        return int(other.subscriber_count) > int(self.subscriber_count)

    def __ge__(self, other):
        return int(other.subscriber_count) >= int(self.subscriber_count)

    def __lt__(self, other):
        return int(other.subscriber_count) <= int(self.subscriber_count)

    def __le__(self, other):
        return int(other.subscriber_count) <= int(self.subscriber_count)

    def __eq__(self, other):
        return int(other.subscriber_count) == int(self.subscriber_count)

