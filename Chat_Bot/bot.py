from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, logging
import torch

model = "TheBloke/Nous-Hermes-Llama-2-7B-GPTQ"

# configure the generator
gen_model = AutoModelForCausalLM.from_pretrained(
    model,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    revision="main"
)

gen_tokenizer = AutoTokenizer.from_pretrained(model, use_fast=True)

pipe = pipeline(
    "text-generation",
    model=gen_model,
    tokenizer=gen_tokenizer,
    max_new_tokens=128,
    repetition_penalty=1.15
)

# configure the POS
logging.set_verbosity(logging.CRITICAL)

# store chat history
chat_history = []

# prompt template string
prompt_template = """Below is an instruction that describes a task. Write a response that appropriately completes the request. 

### Instruction: You are an ai chatbot named chatty. You are in a conversation between you and a friendly human. Continue the conversation.

{history}

### Response:
Omega:
"""

while True:
    # read input & store it
    user_message = input("human: ")
    chat_history.append("human: " + user_message)

    # generate output
    prompt = prompt_template.format(history="\n".join(chat_history))
    out = "chatty: " + pipe(user_message)[0]["generated_text"]

    # store output & print it
    chat_history.append(out)
    print(out)