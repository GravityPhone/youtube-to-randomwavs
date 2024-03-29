import glob
import os

from downloader import download_random_video, search_videos
from snippetmaker import create_snippets
from wavconversion import convert_mp4_to_wav, find_first_mp4


def main(search_term):
    # Search for videos and download one
    search_results = search_videos(search_term)
    if search_results:
        download_random_video(search_results)
    else:
        return "No results found."

    # Find the downloaded video
    input_file = find_first_mp4()
    if input_file:
        # Convert the downloaded video to WAV
        output_file = os.path.splitext(input_file)[0] + ".wav"
        convert_mp4_to_wav(input_file, output_file)

        # Delete the input MP4 file
        os.remove(input_file)

        # Create snippets from the WAV file
        create_snippets(output_file)
    else:
        return "No MP4 files found in the current directory."


if __name__ == "__main__":
    main()
