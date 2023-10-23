import openai as oai
from pynput.keyboard import Key, Controller
from ytchat import chat

oai.api_key = "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"

keyboard = Controller()

messages = []
system_msg = input("Info to input: \n")
messages.append({"role": "system", "content": system_msg})
keyboard.tap(Key.enter)
print("info was entered")

while input != "quit()":
    msg = input(chat)
    keyboard.tap(Key.enter)
    messages.append({"role": "system", "content": msg})
    response = oai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": reply})
    print("\n"+reply+"\n")
    print("reply has been made")