import os

def handle_play_music():
    music_dir = "C:\\Users\\YourUsername\\Music"  # Change path
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
        return "Playing music."
    return "No music found."
