from .open_app import handle_open_app
from .play_music import handle_play_music
from .search_google import handle_search_google
from .fallback_ai import handle_fallback

def handle_command(text):
    text = text.lower()

    if "open" in text:
        return handle_open_app(text)
    elif "play music" in text:
        return handle_play_music()
    elif "search" in text:
        return handle_search_google(text)
    else:
        return handle_fallback(text)
