from gui import setup_gui
from ttkthemes import ThemedTk

def main():
    root = ThemedTk(theme="breeze")  # equilux is a dark theme
    # root.configure(background='#333333')
    # root = tk.Tk()
    root.title("TTS Player")
    setup_gui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
