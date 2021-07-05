# Tkinter is a standard GUI library and it is one of the easiest ways to build a GUI application.
import tkinter as tk
# pytube used for downloading videos from youtube
from pytube import YouTube

# dock is the name of the window

dock = tk.Tk()  # Tk() used to initialize tkinter to create display window
dock.geometry('500x300')  # geometry() used to set the window’s width and height
dock.resizable(0, 0)  # resizable(0,0) set the fix size of window
dock.title("Youtube Video Downloader by Aarshita")  # title() used to give the title of window
tk.Label(dock, text="Youtube Video Downloader",font="arial 20 bold").pack()  # Label() widget use to display text
# that users can’t able to modify.

# Enter the URL
link = tk.StringVar()  # link is a string type variable that stores the youtube video link that the user enters.

tk.Label(dock, text="Paste Link Here:", font="arial 15 bold").place(x=160, y=60)
link_error = tk.Entry(dock, width=70, textvariable=link).place(x=32, y=90)  # Entry() widget is used when we want to create an input text field.


# Function to download the video
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download('D:\Programming')  # Edit it as per your location
    tk.Label(dock, text="Successfully Downloaded", font="arial 15").place(x=180, y=200)


# Download Button
tk.Button(dock, text="DOWNLOAD", font="Verdana 15 bold", bg="orange", padx=2, command=downloader).place(x=180, y=150)

dock.mainloop()
