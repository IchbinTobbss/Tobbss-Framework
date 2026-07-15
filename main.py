import subprocess
import sys
import importlib
print("Initializing...")
print("Done.")
print("Checking for dependencies...")


packages = {
    "arcade": "arcade",
    "pymunk" : "pymunk",
    "ollama" : "ollama",
    "speech_recognition" : "SpeechRecognition",
    "pyttsx3" : "pyttsx3",
    "pyaudio" : "PyAudio",
}

for module, package in packages.items():
    try:
        importlib.import_module(module)
        print(f"{package} is installed")
    except ImportError:
        print(f"Installiere {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Dependencies are installed")
