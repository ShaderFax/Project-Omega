import openai as oai
import sys
sys.path.insert(0, 'p/Project-Omega/speech/ytchat.py')
from ytchat import chatMsg

oai.api_key = "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"

messages = []
system_msg = input("Input: \n")
messages.append({"role": "system", "content": system_msg})

def chatReply():
    while input != "quit()":
        message = input()
        message.append({"role": "system", "content": message})
        response = oai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "system", "content": reply})
        print(reply)