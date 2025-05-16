import webbrowser

def handle_search_google(text):
    query = text.lower().replace("search", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching Google for {query}."
