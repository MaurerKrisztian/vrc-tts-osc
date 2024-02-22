
from pythonosc.udp_client import SimpleUDPClient

def send_text_to_vrchat(text):
    client = SimpleUDPClient("127.0.0.1", 9000)
    print("[osc]: /chatbox/input " + text)
    client.send_message("/chatbox/input", [text, 1, 1])