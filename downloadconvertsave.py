python
import random  
import os
import time
from pytube import YouTube  
from youtube_search import YoutubeSearch
from moviepy.editor import *

def search_videos(search_term):
    search_results = YoutubeSearch(search_term, max_results=500).to_dict()  
    return search_results

from convert_mp4_to_wav import convert_mp4_to_wav  

def download_random_video(search_results):
    video_to_download = None 
    while not video_to_download or video_duration > 1800: 
        video_to_download = random.choice(search_results)
        video_url = f"{video_to_download['url_suffix']}"  
        filename = video_to_download['title']  
        video_duration = duration_in_seconds(video_to_download['duration'])  

    yt = YouTube(video_url)
    yt.streams.first().download(filename=f'{filename}.mp4')
    
    mp4_size = 0
    while mp4_size == 0 or new_size != mp4_size: 
        time.sleep(1)
        new_size = os.path.getsize(f'{filename}.mp4')
        mp4_size = new_size  
        
    print(f'MP4 filename: {filename}.mp4')
    print(f'WAV filename: {filename}.wav')
    
    try: 
        convert_mp4_to_wav(f'{filename}.mp4', f'{filename}.wav')
    except OSError as err:
        print(f"OS error: {err}")  
    except ValueError: 
        print("Error loading MP4 file!")

def convert_mp4_to_wav(input_file, output_file):
    video = VideoFileClip(input_file)  
    audio = video.audio
    audio.write_audiofile(output_file)  
    os.remove(input_file)  

search_term = input("Enter a search term: ")  
search_results = search_videos(search_term)   

if search_results: 
    download_random_video(search_results)    
else:      
    print("No results found.") 