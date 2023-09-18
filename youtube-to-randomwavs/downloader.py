import secrets

from pytube import YouTube


def download_random_video(search_term):
    # Search for videos on YouTube
    search_results = YouTube.search(search_term)

    # Select a random video from the search results
    video_to_download = secrets.choice(search_results)

    # Check if video_to_download is a dictionary with a 'url_suffix' key
    if isinstance(video_to_download, dict) and "url_suffix" in video_to_download:
        # Construct the full URL of the video
        video_url = f"https://www.youtube.com{video_to_download['url_suffix']}"

        # Download the video
        YouTube(video_url).streams.first().download()

        # Return the URL of the downloaded video
        return video_url
    else:
        # If video_to_download is not a dictionary with a 'url_suffix' key, return None
        return None
