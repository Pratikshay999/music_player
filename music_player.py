from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os

# Globals
cwd_path = ''

# Initialize mixer
mixer.init()

# Create the root window
root = Tk()
root.title('Music Player')

# Configure the window size and background color
root.geometry('500x400')
root.configure(bg='lightgray')

# Create a custom font
custom_font = ('Helvetica', 12)

# Create a Listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=custom_font, selectbackground="gray", selectforeground="black")
songs_list.pack(fill=BOTH, expand=True, padx=20, pady=10)

# Function to add songs to the playlist
def addsongs():
    global cwd_path
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_song:
        cwd_path, filename = os.path.split(s)
        songs_list.insert(END, filename)

# Function to delete a selected song
def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song)

# Function to play the selected song
def Play():
    song = songs_list.get(ACTIVE)
    song = f'{cwd_path}/{song}'
    mixer.music.load(song)
    mixer.music.play()

# Function to pause the song
def Pause():
    mixer.music.pause()

# Function to stop the song
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

# Function to resume the song
def Resume():
    mixer.music.unpause()

# Function to navigate to the previous song
def Previous():
    previous_one = songs_list.curselection()
    previous_one = previous_one[0] - 1
    temp2 = songs_list.get(previous_one)
    temp2 = f'{cwd_path}/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)

# Function to navigate to the next song
def Next():
    next_one = songs_list.curselection()
    next_one = next_one[0] + 1
    temp = songs_list.get(next_one)
    temp = f'{cwd_path}/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)

# Create buttons with improved style using pack
play_button = Button(root, text="Play", font=custom_font, command=Play)
pause_button = Button(root, text="Pause", font=custom_font, command=Pause)
stop_button = Button(root, text="Stop", font=custom_font, command=Stop)
resume_button = Button(root, text="Resume", font=custom_font, command=Resume)
previous_button = Button(root, text="Prev", font=custom_font, command=Previous)
next_button = Button(root, text="Next", font=custom_font, command=Next)

# Place buttons using pack
play_button.pack(side=LEFT, padx=10, pady=5)
pause_button.pack(side=LEFT, padx=10, pady=5)
stop_button.pack(side=LEFT, padx=10, pady=5)
resume_button.pack(side=LEFT, padx=10, pady=5)
previous_button.pack(side=LEFT, padx=10, pady=5)
next_button.pack(side=LEFT, padx=10, pady=5)

# Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add Songs", command=addsongs)
add_song_menu.add_command(label="Delete Song", command=deletesong)

# cwd_path =''

# Start the GUI main loop
root.mainloop()
