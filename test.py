import tkinter as tk  # (for GUI interfaces like widgets and buttons)
import customtkinter as ctk  # (extender for tkinter)
from pytube import YouTube  # (to download videos from YouTube via links)

# System settings
ctk.set_appearance_mode("System")  # (for user's operating systems preferences)
ctk.set_default_color_theme("green")  # (color of GUI)

def startDownload():
    try:
        ytLnk = url_var.get()
        ytobject = YouTube(ytLnk)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        status_label.config(text="Download Complete!", fg="green")
    except Exception as e:
        status_label.config(text="Invalid Link or Error Occurred", fg="red")

def openSettings():
    settings_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def closeSettings():
    settings_frame.place_forget()

# App frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Blackhole")

# Set the background color
app.configure(bg="#282c34")  #  desired background color

# UI Elements
title = ctk.CTkLabel(app, text="Insert Link")
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=400, height=30, textvariable=url_var)
link.pack()

# Download button
download = ctk.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Settings button in the upper right corner
settings_button = ctk.CTkButton(app, text="Settings", command=openSettings)
settings_button.place(x=590, y=10)

# Status label to display messages
status_label = ctk.CTkLabel(app, text="")
status_label.pack(padx=10, pady=10)

# Settings frame
settings_frame = ctk.CTkFrame(app, width=300, height=200, corner_radius=10)
settings_label = ctk.CTkLabel(settings_frame, text="Settings")
settings_label.pack(padx=10, pady=10)
close_button = ctk.CTkButton(settings_frame, text="Close", command=closeSettings)
close_button.pack(padx=10, pady=10)

# Initially hide the settings frame
settings_frame.place_forget()

# Run app
app.mainloop()
