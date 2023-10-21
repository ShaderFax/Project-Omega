import os
import openai as oai
import sys
from ytchat import chatMsg

oai.api_key = "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"

messages = []
system_msg = input("Describe the character you want to me to play\n")
messages.append({"role": "system", "content": system_msg})

def chatBot():
    while input != "quit()":
        message = chatMsg
        messages.append({"role": "system", "content": message})
        response = oai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        print("\n"+reply+"\n")
        messages.append({"role": "system", "content": reply})

chatBot()