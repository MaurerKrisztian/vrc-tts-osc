from gui import setup_gui
from ttkthemes import ThemedTk
from whisper_stt import test_stt
def main():
    root = ThemedTk(theme="breeze")
    root.title("TTS Player")
    setup_gui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
