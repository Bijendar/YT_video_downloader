import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Error", "Please enter a YouTube URL")
        return

    try:
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # 1080p max
            'merge_output_format': 'mp4',
            'outtmpl': 'C:/Users/Bijay Rana/Downloads/%(title)s.%(ext)s'  # Change path here
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully at 1080p!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("YotubeDownloader BY Bijendar RANA")
root.geometry("400x150")

# Widgets
tk.Label(root, text="YouTube Video URL:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Button(root, text="Download", command=download, bg="green", fg="white").pack(pady=10)

# Footer Message (Custom)
footer_label = tk.Label(root, text="Made with ❤️ by Bijay Rana", font=("Arial", 8), fg="gray")
footer_label.pack(side="bottom", pady=5)


root.mainloop()
