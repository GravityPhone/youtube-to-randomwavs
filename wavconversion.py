import glob

from moviepy.editor import *


def convert_mp4_to_wav(input_file, output_file):
    try:
        # Load the video file
        video = VideoFileClip(input_file)

        # Extract the audio from the video
        audio = video.audio

        # Write the audio to the output file in WAV format
        audio.write_audiofile(output_file, codec="pcm_s16le")

        return f"Successfully converted {input_file} to {output_file}"
    except Exception as e:
        return f"Error occurred while converting {input_file} to {output_file}. Error: {str(e)}"


def find_first_mp4():
    mp4_files = glob.glob("*.mp4")
    if mp4_files:
        return mp4_files[0]
    else:
        return "No mp4 files found in the current directory"
