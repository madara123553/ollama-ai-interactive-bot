import os

def handle_open_app(text):
    if "chrome" in text:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        return "Opening Chrome."
    elif "notepad" in text:
        os.system("notepad")
        return "Opening Notepad."
    elif "vs code" in text or "vscode" in text:
        os.system("code")
        return "Opening VS Code."
    else:
        return "App not recognized."
