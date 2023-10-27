import openai as oai
from pynput.keyboard import Key, Controller
import pytchat as ytc
import time

oai.api_key = "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"

messages = []
system_msg = input("Info to input: \n")
messages.append({"role": "system", "content": system_msg})

chat = ytc.create(video_id="XxVZYEffgpQ")
while chat.is_alive():
    for c in chat.get().sync_items():
        x = int(c.message)
        for x in range.count(x):
            if x % 5 ():
                print(f"[{c.author.name}]{c.message}\n")
                msg = c.message
                messages.append({"role": "user", "content": msg})
                response = oai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages)
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                print("\n"+reply+"\n")
            elif x !=5 ():
                continue