import openai as oai
import pytchat as ytc

oai.api_key = "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"

messages = []
system_msg = input("Info to input: \n")
messages.append({"role": "system", "content": system_msg})

chat = ytc.create(video_id="XxVZYEffgpQ")
count = 0
while chat.is_alive():
    for c in chat.get().sync_items():
        if count % 5 == 0:
            print(f"[{c.author.name}]{c.message}\n")
            msg = c.message
            messages.append({"role": "user", "content": msg})
            response = oai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("\n"+reply+"\n")
            count += 1
        else:  
            continue

# You are an AI vtuber named Omega-chan