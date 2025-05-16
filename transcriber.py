import sounddevice as sd
import scipy.io.wavfile
import tempfile
from faster_whisper import WhisperModel

model = WhisperModel("base")

def transcribe():
    duration = 5
    fs = 16000
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        scipy.io.wavfile.write(f.name, fs, audio)
        segments, _ = model.transcribe(f.name)
        return " ".join([seg.text for seg in segments])
