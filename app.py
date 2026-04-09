import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSequenceClassification

st.set_page_config(page_title="Jawani AI - Unggah Ungguh", layout="wide")

@st.cache_resource
def load_models():
    # Menggunakan model dari organisasi/repo Hugging Face Anda
    bert_path = "FP-KCV/javanese-honorific-classifier"
    llm_path = "FP-KCV/jawani-sealion-gatra-2-9b"
    
    # Load IndoBERT Classifiers
    b_tokenizer = AutoTokenizer.from_pretrained(bert_path)
    b_model = AutoModelForSequenceClassification.from_pretrained(bert_path).to("cuda")
    
    # Load Sea-Lion LLM (Full Precision float16)
    l_tokenizer = AutoTokenizer.from_pretrained(llm_path)
    l_model = AutoModelForCausalLM.from_pretrained(
        llm_path,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True
    )
    return b_tokenizer, b_model, l_tokenizer, l_model

# Inisialisasi Model
with st.spinner("Nembe nyiapaken otak AI... Monggo dipun tenggo."):
    bert_tok, bert_mod, llm_tok, llm_mod = load_models()

# Mapping Label
honorific_map = {0: "Ngoko Lugu", 1: "Ngoko Alus", 2: "Krama Lugu", 3: "Krama Inggil"}

# UI Sidebar
st.sidebar.header("Setelan Persona")
persona = st.sidebar.selectbox(
    "Pilih Peran AI:",
    ["Guru Basa Jawa", "Kanca Cerak", "Asisten Resmi"]
)

persona_prompts = {
    "Guru Basa Jawa": "Panjenengan minangka Guru Basa Jawa. Gunakake basa Krama Inggil lan paring koreksi menawi siswa salah.",
    "Kanca Cerak": "Kowe dadi kanca cerak sing asik. Gunakake basa Ngoko Lugu sing santai.",
    "Asisten Resmi": "Anda adalah asisten formal yang menggunakan basa Krama Lugu."
}

# Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Sugeng siang, wonten ingkang saged kula biyantu?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 1. Klasifikasi Unggah-Ungguh
    b_inputs = bert_tok(prompt, return_tensors="pt").to("cuda")
    with torch.no_grad():
        b_logits = bert_mod(**b_inputs).logits
    label = honorific_map.get(b_logits.argmax().item(), "Ngoko Lugu")

    # 2. Generasi Respon Berdasarkan Persona
    with st.chat_message("assistant"):
        context = f"Instruction: {persona_prompts[persona]}\nUser (Detected: {label}): {prompt}\nAI Response:"
        l_inputs = llm_tok(context, return_tensors="pt").to("cuda")
        
        with torch.no_grad():
            outputs = llm_mod.generate(
                **l_inputs,
                max_new_tokens=256,
                temperature=0.7,
                do_sample=True,
                pad_token_id=llm_tok.eos_token_id
            )
        
        raw_res = llm_tok.decode(outputs[0], skip_special_tokens=True)
        res = raw_res.split("AI Response:")[-1].strip()
        
        st.caption(f"Deteksi Sistem: {label}")
        st.markdown(res)
        st.session_state.messages.append({"role": "assistant", "content": res})