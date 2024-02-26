from gui import setup_gui
from ttkthemes import ThemedTk
from whisper_stt import test_stt
import multiprocessing

def main():
    root = ThemedTk(theme="breeze")
    root.title("TTS Player")
    root.geometry("400x1100")
    setup_gui(root)
    root.mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    # test_stt()
    main()
