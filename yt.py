from tkinter import *
from pytube import YouTube
import os


root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("DataFlair-youtube video downloader")

Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()
Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def DownloadeVid():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


def DownloadeAud():
    url = YouTube(str(link.get()))
    video = url.streams.filter(only_audio=True).first()
    file = video.download()
    base, ext = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD VIDEO', font='arial 15 bold', bg='pale violet red',
       padx=2, command=DownloadeVid).place(x=59, y=150)

Button(root, text='DOWNLOAD MP3', font='arial 15 bold', bg='pale violet red',
       padx=2, command=DownloadeAud).place(x=300, y=150)
root.mainloop()
