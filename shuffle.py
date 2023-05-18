import os
import numpy as np
import pygame
from pygame import mixer

songs_folder = "C:/Users/Gunethra/Documents/AI-sw/Content"

def song_shuffler(songs):
    songs = np.array(songs)
    num_songs = len(songs)
    shuffled_songs = np.empty_like(songs)
    index_pool = np.arange(num_songs)

    np.random.shuffle(index_pool)

    for i in range(num_songs):
        shuffled_songs[i] = songs[index_pool[i]]
        if i < num_songs - 1:
            np.delete(index_pool, np.where(index_pool == index_pool[i]))

    return shuffled_songs

songs = ['IMG_0553.wav', 'IMG_0555.wav', 'IMG_0556.wav', 'IMG_0557.wav', 'IMG_0558.wav', 'IMG_0559.wav', 'IMG_0560.wav', 'IMG_0561.wav', 'IMG_0562.wav', 'IMG_0563.wav', 'IMG_0565.wav', 'IMG_0566.wav', 'IMG_0567.wav', 'IMG_0568.wav', 'IMG_0569.wav', 'IMG_0570.wav', 'IMG_0571.wav', 'IMG_0572.wav', 'IMG_0574.wav', 'IMG_0575.wav']
shuffled_songs = song_shuffler(songs)

def play_songs(songs):
    pygame.mixer.init()
    for song in songs:
        print("Now playing:", song)
        song_path = os.path.join(songs_folder, song)
        print("From:", song_path)
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            print('***********************************************************************')
            command = input("Enter command (pause/resume/next/quit): ")

            if command.lower() == "pause":
                pygame.mixer.music.pause()
                pause()
            elif command.lower() == "resume":
                print("Song not paused!")
                # pygame.mixer.music.unpause()
            elif command.lower() == "next":
                pygame.mixer.music.stop()
                break
            elif command.lower() == "quit":
                # pygame.mixer.music.stop()
                # pygame.mixer.quit()
                quit()
                return

def pause():
    print("Paused")
    print('***********************************************************************')
    pause_command = input("Enter command (pause/resume/next/quit): ")

    if pause_command.lower() == "resume":
        print("Resuming...")
        pygame.mixer.music.unpause()
    elif pause_command.lower() == "next":
        pygame.mixer.music.stop()
        
    elif pause_command.lower() == "quit":
        # pygame.mixer.music.stop()
        # pygame.mixer.quit()
        quit()
        return

for song in shuffled_songs:
    # print(song)
    print('***********************************************************************')
    play_songs(shuffled_songs)
