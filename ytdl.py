import tkinter as tk
from tkinter import messagebox, filedialog
#from youtube_dl import YoutubeDL
from yt_dlp import YoutubeDL


# Step 1: Create GUI
root = tk.Tk()

text_area = tk.Text(root)
text_area.pack()

def download_videos():
    urls = text_area.get('1.0', 'end-1c').split('\n')
    download_path = filedialog.askdirectory()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': download_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download([url])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download {url}. Reason: {str(e)}")

button = tk.Button(root, text="Download as MP3", command=download_videos)
button.pack()

root.mainloop()
