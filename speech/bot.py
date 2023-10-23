import os
import openai as oai
import sys
from ytchat import chat

oai.api_key = "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"

messages = [{
      "role": "system",
      "content": "You are an ai vtuber called omega-chan, you are enthusiastic."
    }]
system_msg = ""
messages.append({"role": "system", "content": system_msg})

while input != "quit()":
    msg = input()
    messages.append({"role": "system", "content": msg})
    response = oai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": reply})
    print("\n"+reply+"\n")