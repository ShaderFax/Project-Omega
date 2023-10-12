import pytchat as ytc

# install pytchat w/ "py -m pip install pytchat"

chat = ytc.create(video_id="")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.message}")