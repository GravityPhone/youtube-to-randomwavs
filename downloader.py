import random

from pytube import YouTube
from youtube_search import YoutubeSearch


def search_videos(search_term):
    search_results = YoutubeSearch(search_term, max_results=500).to_dict()
    return str(search_results)


def duration_in_seconds(duration_str):
    duration_parts = str(duration_str).split(":")
    if len(duration_parts) == 3:
        hours, minutes, seconds = map(int, duration_parts)
        return hours * 3600 + minutes * 60 + seconds
    else:
        minutes, seconds = map(int, duration_parts)
        return minutes * 60 + seconds


def download_random_video(search_results):
    video_to_download = None
    video_duration = None

    while not video_to_download or (video_duration and video_duration > 1800):
        video_to_download = random.choice(search_results)
        video_url = f"https://www.youtube.com{video_to_download['url_suffix']}"
        video_title = video_to_download["title"]
        video_duration = duration_in_seconds(video_to_download.get("duration"))

    yt = YouTube(video_url)
    video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

    video_stream.download(filename=f"{video_title}.mp4")
    return f"Video downloaded: {video_title}.mp4"
