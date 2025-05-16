import whisper
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile

model = whisper.load_model("base")

def record_audio(duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return audio, fs

def save_audio(audio, fs):
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    scipy.io.wavfile.write(tmp.name, fs, audio)
    return tmp.name

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
