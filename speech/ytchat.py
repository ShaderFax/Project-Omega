import pytchat as ytc
import time

# install pytchat w/ "py -m pip install pytchat"

def chatMsg():
    chat = ytc.create(video_id="")
    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.message}")
            time.sleep(30)

chatMsg()