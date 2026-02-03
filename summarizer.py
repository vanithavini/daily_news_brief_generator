import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "t5-small"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

def summarize(text, short=False):
    tokenizer, model = load_model()

    input_text = "summarize: " + text
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # 🔑 control summary length
    if short:
        max_tokens = 60
    else:
        max_tokens = 140

    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_new_tokens=max_tokens,
            do_sample=False
        )

    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary
