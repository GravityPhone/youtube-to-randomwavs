import os
import glob
import random
from pydub import AudioSegment
import os
import glob
import random
from pydub import AudioSegment

def create_snippets(wav_file):
    # Logic to create snippets
    pass
# Search for wav files in the current directory
wav_files = glob.glob("./*.wav")

# Create a new directory called "snippets" if it doesn't exist
if not os.path.exists("snippets"):
    os.makedirs("snippets")

# Create 10-second snippets from the found wav files, 
# and export them to the "snippets" directory
snippet_counter = 1
while snippet_counter <= 10:
    wav_file = random.choice(wav_files)
    audio = AudioSegment.from_wav(wav_file) 

    # Make sure the audio is at least 10 seconds long, 
    # and that the snippet doesn't go past the end of the audio
    if len(audio) >= 10000 and len(audio) - 10000 > 0:
        # Select a random starting point for the snippet
        max_start = len(audio) - 10000
        start = random.randint(0, max_start)
        snippet = audio[start : start + 10000]

        # Generate snippet file name
        snippet_name = f"snippet{snippet_counter}.wav"
        snippet_path = os.path.join("snippets", snippet_name)

        # Check if the file already exists, and find the next available number
        while os.path.exists(snippet_path):
            snippet_counter += 1
            snippet_name = f"snippet{snippet_counter}.wav"
            snippet_path = os.path.join("snippets", snippet_name)

        # Export the snippet to the new file
        snippet.export(snippet_path, format="wav")
        print(f"Exported {snippet_path}")

        # Increment the snippet counter for the next iteration
        snippet_counter += 1
