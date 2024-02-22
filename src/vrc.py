
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("127.0.0.1", 9000)

def send_text_to_vrchat(text):
    print("[osc]: /chatbox/input " + text)
    client.send_message("/chatbox/input", [text, 1, 1])


def typing(b):
    client.send_message("/chatbox/typing", [b])

