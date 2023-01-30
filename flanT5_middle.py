from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

prompt = input("Put in your prompt:")

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")

min_length=20
max_new_tokens=500
length_penalty=3.0
num_beams=5
no_repeat_ngram_size=5
temperature=1.9
top_k=300
top_p=0.9
repetition_penalty=3.0

input = tokenizer(prompt, return_tensors="pt")
generate = model.generate(**input, min_length=min_length, max_new_tokens=max_new_tokens, length_penalty=length_penalty, num_beams=num_beams, no_repeat_ngram_size=no_repeat_ngram_size, temperature=temperature, top_k=top_k, top_p=top_p, repetition_penalty=repetition_penalty,)
output = str(tokenizer.batch_decode(generate, skip_special_tokesn=True))
parse=output[8:-6]
print(parse)
