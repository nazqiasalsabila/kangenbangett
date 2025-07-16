import streamlit as st
import random
import time
import requests
from datetime import date

# ---------- Config ----------
st.set_page_config(page_title="Jars of Happiness 💖", layout="centered")

# ---------- Styling ----------
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .title {
        text-align: center;
        font-size: 40px;
        color: #ff69b4;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #db7093;
    }
    .message-box {
        background-color: #ffe4e1;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 20px;
        color: #c71585;
        box-shadow: 2px 2px 10px pink;
    }
    .blink {
        animation: blinker 1s linear infinite;
    }
    @keyframes blinker {
        50% { opacity: 0.3; }
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<div class='title'>🫙 Jars of Happiness 💖</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Klik toples ini untuk ambil 1 kebahagiaan hari ini ✨</div>", unsafe_allow_html=True)

# ---------- Animation GIF ----------
st.image("https://media.giphy.com/media/f9k1tV7HyORcngKF8v/giphy.gif", use_column_width=True)

# ---------- Session State ----------
if "last_open" not in st.session_state:
    st.session_state.last_open = ""

# ---------- Messages ----------
pesan_kebahagiaan = [
    "Kamu adalah alasan kenapa aku senyum hari ini 😘",
    "Hari ini mungkin berat, tapi kamu lebih kuat 💪",
    "Senyummu lebih manis dari boba milk tea 💗",
    "Kalau dunia jahat, sini aku peluk 🤗",
    "Kamu tuh kayak sinyal WiFi — bikin hidup nyambung 🌐",
    "Ingat, kamu dicintai lebih dari yang kamu kira 💞",
    "Kamu layak bahagia, bahkan di hari yang biasa 💐",
    "Pakai ini buat recharge semangatmu ya 🔋",
    "Aku bangga sama kamu hari ini ✨",
    "Semoga ini bikin kamu senyum sedikit aja 😊",
]

# ---------- Date check ----------
hari_ini = str(date.today())

# ---------- Button ----------
st.markdown("\n")
if st.button("🎁 Ambil Catatan Hari Ini", use_container_width=True):
    if st.session_state.last_open != hari_ini:
        with st.spinner("Lagi buka jar kamu... 🎀"):
            time.sleep(2)
        pesan = random.choice(pesan_kebahagiaan)
        st.session_state.last_open = hari_ini
        st.markdown(f"<div class='message-box blink'>💌 {pesan}</div>", unsafe_allow_html=True)
    else:
        st.warning("Udah dibuka hari ini yaa 😗\nBesok balik lagi yaa~ 💖")

# ---------- Footer ----------
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 14px; color: gray;'>
    Aplikasi ini adalah hadiah kecil, dari aku yang (masih) cinta kamu 💝
    </p>
""", unsafe_allow_html=True)
