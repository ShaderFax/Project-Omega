from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none
from IPython.display import display, Audio
from playsound import playsound as ps
import time
import torch
import soundfile as sf
from bot import reply

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

# input from OpenAI bot
x = reply

# synthesis
with torch.no_grad():
    start = time.time()
    wav = text2speech(x)["wav"]
elapsed = (time.time() - start)
print(f"elapsed = {elapsed:5f}")

# save it!
sf.write("out.wav", wav.view(-1).cpu().numpy(), text2speech.fs, "PCM_16")
ps('P:\Project-Omega\speech\out.wav')