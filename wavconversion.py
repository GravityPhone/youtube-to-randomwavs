import os
import glob
from moviepy.editor import *

def convert_mp4_to_wav(input_file, output_file):
    # Load the video file
    video = VideoFileClip(input_file)

    # Extract the audio from the video
    audio = video.audio

    # Write the audio to the output file in WAV format
    audio.write_audiofile(output_file, codec='pcm_s16le')

def find_first_mp4():
    mp4_files = glob.glob('*.mp4')
    return mp4_files[0] if mp4_files else None
