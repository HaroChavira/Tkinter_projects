import tkinter
from tkinter import font
import pyshorteners

root = tkinter.Tk()
root.title ("URL Shortener")
root.geometry("400x150")

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0, short_url)

longurl_label = tkinter.Label(root, text="Enter Long URL", font=("Small Fonts", 12))
longurl_entry = tkinter.Entry(root, font=("Small Fonts", 12))
shorturl_label = tkinter.Label(root, text="Output Shortend URL", font=("Small Fonts", 12))
shorturl_entry = tkinter.Entry(root, font=("Small Fonts", 12))
shorten_button = tkinter.Button(root, text="Shorten URL", font=("Small Fonts", 12), command=shorten)

longurl_label.grid(row=1, column=0)
longurl_entry.grid(row=1, column=1)
shorturl_label.grid(row=2,column=0)
shorturl_entry.grid(row=2, column=1)
shorten_button.grid(row=3, column=1)


root.mainloop()