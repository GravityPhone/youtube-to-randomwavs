import tkinter as tk
from tkinter import messagebox

from downloader import download_random_video


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.search_entry = tk.Entry(self)
        self.search_entry.pack(side="top")

        self.download_button = tk.Button(self)
        self.download_button["text"] = "Download"
        self.download_button["command"] = self.download
        self.download_button.pack(side="top")

    def download(self):
        search_term = self.search_entry.get()
        results = download_random_video(search_term)

        # Check if results is None or an empty dictionary
        if not results or not isinstance(results, dict):
            messagebox.showerror("Error", "No video found for the given search term.")
            return

        results["url_suffix"]
        # Rest of the download logic...
