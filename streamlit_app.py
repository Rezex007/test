import streamlit as st
import time
import random

# ---------- CONFIG ----------
st.set_page_config(page_title="น้ำอิง... มีไรจะบอก 🤫", layout="centered")

# ---------- CSS (Full Effects & Animations) ----------
st.markdown("""
<style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #1a012e, #4b0082, #9400d3, #1a012e);
        background-size: 400% 400%;
        animation: gradientBG 8s ease infinite;
        color: white;
        overflow-x: hidden;
    }

    @keyframes floatHeart {
        0% { transform: translateY(110vh) rotate(0deg) scale(0.5); opacity: 0; }
        20% { opacity: 0.8; }
        80% { opacity: 0.8; }
        100% { transform: translateY(-20vh) rotate(720deg) scale(1.5); opacity: 0; }
    }

    .heart {
        position: fixed;
        bottom: -10%;
        user-select: none;
        pointer-events: none;
        z-index: 1;
        animation: floatHeart linear infinite;
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
        40% {transform: translateY(-20px);}
        60% {transform: translateY(-10px);}
    }

    .bounce-text {
        animation: bounce 1s ease;
    }

    .content-wrapper {
        text-align: center;
        background: transparent;
        z-index: 10;
        position: relative;
        padding: 10px;
    }

    .main-title {
        color: #d8b4fe;
        font-size: clamp(35px, 8vw, 65px);
        font-weight: 900;
        text-shadow: 0 0 30px rgba(216, 180, 254, 1);
        margin-bottom: 10px;
    }

    /* ปุ่มแบบมี Glow */
    div.stButton > button {
        border-radius: 50px;
        border: 3px solid #ff69b4 !important;
        background: rgba(255, 105, 180, 0.2) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold;
        height: auto;
        padding: 15px 30px;
        transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 0 20px rgba(255, 105, 180, 0.4);
    }

    .gif-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }

    .gif-container img {
        width: 100%;
        max-width: 500px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
</style>
""", unsafe_allow_html=True)

# ---------- MEGA FLOATING HEARTS ----------
heart_icons = ["💖", "💗", "💘", "💝", "✨"]
heart_html = ""
for i in range(40):
    left = random.randint(0, 100)
    size = random.randint(20, 40)
    duration = random.uniform(4, 8)
    delay = random.uniform(0, 5)
    icon = random.choice(heart_icons)
    heart_html += f'<div class="heart" style="left:{left}%; font-size:{size}px; animation-duration:{duration}s; animation-delay:-{delay}s;">{icon}</div>'
st.markdown(heart_html, unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = "start"
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

# ---------- UI LOGIC ----------
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

if st.session_state.step == "start":
    title_class = "main-title bounce-text" if st.session_state.no_clicks > 0 else "main-title"
    st.markdown(f'<div class="{title_class}">เป็นแฟนกันมั้ยน้ำอิง 💖</div>', unsafe_allow_html=True)
    
    # GIF หน้าแรก (แก้ให้โหลดชัวร์บนมือถือ)
    st.markdown("""
        <div class="gif-container">
            <img src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif">
        </div>
    """, unsafe_allow_html=True)
    
    yes_scale = 1 + (st.session_state.no_clicks * 2.5)
    col1, col2 = st.columns([yes_scale, 1])

    with col1:
        if st.button("ตกลง 💖", use_container_width=True):
            st.session_state.step = "reveal"
            st.rerun()

    with col2:
        no_labels = ["ไม่เอา", "หือ?", "เอาใหม่ดิ", "แน่ใจนะ?", "กดผิดป่าว?", "ยอมเหอะน้ำอิง!"]
        current_label = no_labels[min(st.session_state.no_clicks, len(no_labels)-1)]
        if st.button(current_label, use_container_width=True):
            st.session_state.no_clicks += 1
            st.rerun()

elif st.session_state.step == "reveal":
    st.markdown('<div class="main-title bounce-text" style="color:#FF69B4;">SURPRISE! ✨</div>', unsafe_allow_html=True)
    
    gif_placeholder = st.empty()
    msg_placeholder = st.empty()
    sub_placeholder = st.empty()

    # 1. แสดงแมวหลอก
    gif_placeholder.markdown("""
        <div class="gif-container">
            <img src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif">
        </div>
    """, unsafe_allow_html=True)
    msg_placeholder.markdown('<div style="font-size: 35px; font-weight: 900; color: #FFF; text-shadow: 0 0 20px #FF69B4;">เป็นแฟนเค้าแล้วนะเบบี๋ 💖</div>', unsafe_allow_html=True)
    
    time.sleep(2.0)
    
    # 2. หักมุมเปลี่ยนเป็นตัวตลก (แก้ให้โหลดชัวร์บนมือถือ)
    gif_placeholder.markdown("""
        <div class="gif-container">
            <img src="https://media.giphy.com/media/ZFzmkEqVFpVz02RU3j/giphy.gif">
        </div>
    """, unsafe_allow_html=True)
    
    full_text = "Happy April Fool's Dayคับน้ำอิง 😏"
    current_msg = ""
    for char in full_text:
        current_msg += char
        msg_placeholder.markdown(f'<div class="bounce-text" style="font-size: 38px; font-weight: 900; color: #FFEA20; text-shadow: 3px 3px #000;">{current_msg}</div>', unsafe_allow_html=True)
        time.sleep(0.08)

    sub_placeholder.markdown('<div style="font-size: 22px; color: #fff; margin-top: 15px; font-weight:bold; background:rgba(0,0,0,0.3); border-radius:20px; padding:15px;">ตั๋วโดนคนเจียงใหม่วอกแล้วน้ำอิง สมน้ำหน้า🤪</div>', unsafe_allow_html=True)

    st.balloons()
    time.sleep(0.5)
    st.snow()
    
    st.markdown('<div style="color: #ccc; font-style: italic; margin-top: 50px;">(โดนแกงจั๊ดหนัก 😜)</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
