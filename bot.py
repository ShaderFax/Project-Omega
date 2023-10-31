from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none
from IPython.display import display, Audio
from playsound import playsound as ps
import logging
import os
import uuid
import time
import torch
import soundfile as sf
import openai as oai
import pytchat as ytc

# logging.basicConfig(level=logging.DEBUG)
oai.api_key = "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"

messages = []
system_msg = input("Info to input: \n")
messages.append({"role": "system", "content": system_msg})

chat = ytc.create(video_id="XxVZYEffgpQ")
i = 0
while chat.is_alive():
    for c in chat.get().sync_items():
        if i % 3==0:
            print(f"[{c.author.name}]{c.message}\n")
            msg = c.message
            messages.append({"role": "user", "content": msg})
            response = oai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                tempurature=0.5)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("\n"+reply+"\n")
            
            tag = 'kan-bayashi/ljspeech_tacotron2'
            vocoder_tag = "parallel_wavegan/ljspeech_hifigan.v1"

            text2speech = Text2Speech.from_pretrained(
                model_tag=str_or_none(tag),
                vocoder_tag=str_or_none(vocoder_tag),
                device="cuda",
                # Only for Tacotron 2 & Transformer
                threshold=0.5,
                # Only for Tacotron 2
                minlenratio=0.0,
                maxlenratio=10.0,
                use_att_constraint=False,
                backward_window=1,
                forward_window=3,
                # Only for FastSpeech & FastSpeech2 & VITS
                #speed_control_alpha=1.0,
                # Only for VITS
                #noise_scale=0.333,
                #noise_scale_dur=0.333,
            )

            # synthesis
            with torch.no_grad():
                start = time.time()
                wav = text2speech(reply)["wav"]
            elapsed = (time.time() - start)
            print(f"elapsed = {elapsed:5f}")

            print("generated audio\n")

            # save it!
            filename=str(uuid.uuid4())
            sf.write(f"{filename}.wav", wav.view(-1).cpu().numpy(), text2speech.fs, "PCM_16")
            ps(f"{filename}.wav")

            print("Sound played\n")
            
            os.remove(f"{filename}.wav")
            print("removed\n")

            i += 1
        else:
            i += 1
            continue

# You are an AI vtuber named Omega-chan