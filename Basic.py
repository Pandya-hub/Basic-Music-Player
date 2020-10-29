from tkinter import *
import os
from tkinter.filedialog import askdirectory
import pygame
from IPython.terminal.pt_inputhooks import tk
import mutagen

from mutagen.id3 import ID3

root = Tk()

root.minsize(500,500)                                   # Size of the GUI window
listofsongs = []
realnames = []
index = 0

v = StringVar()
songlabel = Label(root, textvariable = v, width = 35)

def nextSong(event):
    global index
    index +=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def previoussong(event):
    global index
    index -=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname

def updatelabel():
    global index
    global songname
    songname = v.set(realnames[index])
    return songname

def directoryChooser():

    directory = askdirectory()                          # Asking the permission for opening a directory
    os.chdir(directory)                                 # Changing the current directory to the chosen directory

    for files in os.listdir(directory):
        if files.endswith(".mp3"):                      # Check the file extension

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])

            listofsongs.append(files)                   # Append the MP3 file in a list0
directoryChooser()
pygame.mixer.init()                                     # Initialize the mixer module of pygame.
pygame.mixer.music.load(listofsongs[0])                 # Load the song at index[0]
                                                        # Play the song loaded.( pygame.mixer.music.play() )

label = Label(root, text = "Music player")
label.pack()

listbox = Listbox(root)
listbox.pack()

realnames.reverse()

for items in realnames:
    listbox.insert(0,items)
realnames.reverse()

nextBtn = Button(root, text = "Next Song")
nextBtn.pack(padx = 5, pady = 10, side=LEFT)

previousBtn = Button(root, text = "Previous Song")
previousBtn.pack(padx = 5, pady = 20, side=LEFT)

stopBtn = Button(root, text = "Stop Music")
stopBtn.pack(padx = 5, pady = 30, side=LEFT)

nextBtn.bind("<Button-1>",nextSong)
previousBtn.bind("<Button-1>",previoussong)
stopBtn.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()
