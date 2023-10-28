import os
from googleapiclient.discovery import build


class Video:
    youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))

    def __init__(self, video_id: str) -> None:
        try:
            self.video_id = video_id
            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=video_id).execute()
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.url = f'https://youtu.be/{video_id}'
            self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            self.video_id = video_id
            self.video_response = None
            self.title: str = None
            self.url = None
            self.comment_count: int = None
            self.like_count: int = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id
