import pytchat as ytc
from pynput.keyboard import Key, Controller

KB = Controller()

chat = ytc.create(video_id="XxVZYEffgpQ")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"[{c.author.name}]{c.message}\n")
        KB.tap(Key.enter)