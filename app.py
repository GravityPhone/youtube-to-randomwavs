import tkinter as tk
from tkinter import messagebox

import downloader
import snippetmaker
import wavconversion


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube to Random WAVs")

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.text = tk.Text(self)
        self.text.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.pack()

        self.download_button = tk.Button(self, text="Download", command=self.download)
        self.download_button.pack()

        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.snippet_button = tk.Button(
            self, text="Create Snippets", command=self.create_snippets
        )
        self.snippet_button.pack()

    def search(self):
        search_term = self.entry.get()
        results = downloader.search_videos(search_term)
        self.text.insert(tk.END, results)

    def download(self):
        search_term = self.entry.get()
        results = downloader.download_random_video(search_term)
        self.text.insert(tk.END, results)

    def convert(self):
        input_file = wavconversion.find_first_mp4()
        if input_file:
            output_file = wavconversion.convert_mp4_to_wav(input_file)
            self.text.insert(tk.END, output_file)
        else:
            messagebox.showerror(
                "Error", "No MP4 files found in the current directory."
            )

    def create_snippets(self):
        wav_file = wavconversion.find_first_mp4().replace(".mp4", ".wav")
        if wav_file:
            results = snippetmaker.create_snippets(wav_file)
            self.text.insert(tk.END, results)
        else:
            messagebox.showerror(
                "Error", "No WAV files found in the current directory."
            )


if __name__ == "__main__":
    app = Application()
    app.mainloop()
