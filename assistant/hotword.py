import pvporcupine
import pyaudio
import struct

def wait_for_hotword():
    access_key = "I6JUATPcToyRi1doaw1+DpILlL+GCzGNpzyW4qMcy1i91u0YF/VkZA==" 

    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=None,
        keywords=["hey google"]
    )
