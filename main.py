import subprocess
import sys
import importlib


print("Initializing...")
print("Done.")

packages = {
    "arcade": "arcade",
    "pymunk": "pymunk",
    "ollama": "ollama",
    "speech_recognition": "SpeechRecognition",
    "pyttsx3": "pyttsx3",
    "pyaudio": "PyAudio",
}


def install_dependencies():
    print("Checking for dependencies...")

    for module, package in packages.items():
        try:
            importlib.import_module(module)
            print(f"{package} is installed")

        except ImportError:
            print(f"Installing {package}...")

            subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                package
            ])

    print("Dependencies are installed")


def main():
    if "--install" in sys.argv:
        install_dependencies()
        return

    print("Tobi Framework started")


if __name__ == "__main__":
    main()
