import os
import glob
from downloader import search_videos, download_random_video
from wavconversion import convert_mp4_to_wav
from snippetmaker import create_snippets

def main():
    # Ask the user for a search term
    search_term = input("Enter a search term: ")

    # Search for videos and download one
    search_results = search_videos(search_term)
    if search_results:
        video_title = download_random_video(search_results)
    else:
        print("No results found.")
        return

    # Find the downloaded video
    mp4_files = glob.glob('*.mp4')
    input_file = mp4_files[0] if mp4_files else None

    if input_file:
        # Convert the downloaded video to WAV
        output_file = os.path.splitext(input_file)[0] + ".wav"
        convert_mp4_to_wav(input_file, output_file)

        # Delete the input MP4 file
        os.remove(input_file)

        # Create snippets from the WAV file
        create_snippets(output_file)
    else:
        print("No MP4 files found in the current directory.")

if __name__ == "__main__":
    main()