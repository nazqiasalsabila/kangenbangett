import streamlit as st
import time
import random

st.set_page_config(page_title="💗 Tombol Darurat Kangen 💗", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .big-button {
        font-size: 30px !important;
        padding: 20px 40px;
        background-color: #ff69b4;
        color: white;
        border-radius: 15px;
        border: none;
        font-weight: bold;
        box-shadow: 2px 2px 10px pink;
        text-align: center;
        width: 100%;
    }
    .love-blink {
        animation: blink 0.8s infinite;
    }
    @keyframes blink {
        0%   { color: #ff69b4; }
        50%  { color: #ff1493; }
        100% { color: #ff69b4; }
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown("""
    <h1 style='text-align: center; color: #ff1493;'>💖 Tombol Darurat Kangen 💖</h1>
    <p style='text-align: center; font-size: 22px;'>Kalau kamu pencet ini, kamu 100% bucin 😆</p>
""", unsafe_allow_html=True)

# Kumpulan pesan bucin random
pesan_kangen = [
    "Aku juga kangen kamu banget 😭💕",
    "Gimana sih caranya biar bisa peluk kamu sekarang? 🥺",
    "Duh, kenapa kamu gemes banget sih 😤❤️",
    "Level kangen kamu: NGGAK TERBATAS 💘",
    "Kangennya sampe bikin kupu-kupu di perut demo 🙈",
    "Nih peluk 100x buat kamu 🤗🤗🤗🤗🤗",
]

# Tombol besar
if st.button("😭 AKU KANGEN BANGET 😭", key="kangen_button"):
    # Efek animasi teks "BOOM!"
    for i in range(3):
        st.markdown("<h2 class='love-blink' style='text-align: center;'>💥 BOOM! 💥</h2>", unsafe_allow_html=True)
        time.sleep(0.3)

    # Tampilkan pesan kangen lucu
    st.markdown(f"<h3 style='text-align: center; color: #d63384;'>{random.choice(pesan_kangen)}</h3>", unsafe_allow_html=True)

    # Peluk digital
    st.image("https://media.tenor.com/MlXNjHFiHhcAAAAC/hug-cute.gif", caption="Peluk dari aku 🥹", use_column_width=True)

else:
    # Tampilan awal: gif nungguin
    st.image("https://media.tenor.com/3FvgsDG02xoAAAAi/bubu-dudu.gif", width=200)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Lagi nunggu peluk dari kamu nih... 😗</p>", unsafe_allow_html=True)

# Catatan manis di bawah
st.markdown("""
    <p style='text-align: center; color: gray; font-size: 14px;'>
    Buka ini kapan pun kamu pengen peluk virtual dari aku. <br> 
    Dijamin no drama, cuma cinta. 🧸✨
    </p>
""", unsafe_allow_html=True)
