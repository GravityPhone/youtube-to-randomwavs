import os
import glob
import random
from pydub import AudioSegment

def create_snippets(wav_file):
    # Extract the base name of the wav file without the extension
    base_name = os.path.splitext(os.path.basename(wav_file))[0]

    # Create a new directory with the base name if it doesn't exist
    dir_name = os.path.join("snippets", base_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Create 10-second snippets from the provided wav file, 
    # and export them to the new directory
    snippet_counter = 1
    audio = AudioSegment.from_wav(wav_file) 

    while snippet_counter <= 10:
        # Select a random starting point for the snippet
        max_start = len(audio) - 10000
        if max_start > 0:
            start = random.randint(0, max_start)
        else:
            start = 0
        snippet = audio[start : start + 10000]

        # Generate snippet file name
        snippet_name = f"{base_name}_snippet{snippet_counter}.wav"
        snippet_path = os.path.join(dir_name, snippet_name)

        # Export the snippet to the new file
        snippet.export(snippet_path, format="wav")
        print(f"Exported {snippet_path}")

        # Increment the snippet counter for the next iteration
        snippet_counter += 1

    # Delete the original wav file
    os.remove(wav_file)


