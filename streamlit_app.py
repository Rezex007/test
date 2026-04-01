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

    .content-wrapper {
        text-align: center;
        background: transparent;
        z-index: 10;
        position: relative;
    }

    .main-title {
        color: #d8b4fe;
        font-size: clamp(35px, 8vw, 65px);
        font-weight: 900;
        text-shadow: 0 0 30px rgba(216, 180, 254, 1);
    }

    div.stButton > button {
        border-radius: 50px;
        border: 3px solid #ff69b4 !important;
        background: rgba(255, 105, 180, 0.2) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold;
        padding: 15px 30px;
        transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .gif-container img {
        width: 100%;
        max-width: 500px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------- MEGA FLOATING HEARTS ----------
heart_icons = ["💖", "💗", "💘", "💝", "✨"]
heart_html = "".join([
    f'<div class="heart" style="left:{random.randint(0, 100)}%; font-size:{random.randint(20, 40)}px; '
    f'animation-duration:{random.uniform(4, 8)}s; animation-delay:-{random.uniform(0, 5)}s;">{random.choice(heart_icons)}</div>'
    for _ in range(45)
])
st.markdown(heart_html, unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = "start"
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

# ---------- MAIN INTERFACE (ใช้ empty เพื่อป้องกันการซ้อน) ----------
main_container = st.empty()

with main_container.container():
    if st.session_state.step == "start":
        st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
        st.markdown(f'<div class="main-title">เป็นแฟนกันมั้ยน้ำอิง 💖</div>', unsafe_allow_html=True)
        st.markdown('<div class="gif-container"><img src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"></div>', unsafe_allow_html=True)
        
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
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.step == "reveal":
        # จังหวะที่ 1: ดีใจเก้อ
        st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
        st.markdown('<div class="main-title" style="color:#FFF;">เย้! ✨</div>', unsafe_allow_html=True)
        st.markdown('<div class="gif-container"><img src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"></div>', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 40px; font-weight: 900; color: #FFF; text-shadow: 0 0 20px #FF69B4;">เป็นแฟนเค้าแล้วนะเบบี๋ 💖</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        time.sleep(2.0)

        # จังหวะที่ 2: เคลียร์จอเบรกอารมณ์ (ใช้การล้าง main_container)
        main_container.empty()
        time.sleep(0.1) # เคลียร์สั้นๆ
        with main_container.container():
            st.markdown('<div style="height: 250px;"></div>', unsafe_allow_html=True)
            st.markdown('<div style="font-size: 32px; font-weight: bold; color: #d8b4fe; text-align: center;">ถามว่าเรื่องจริงหรออ...</div>', unsafe_allow_html=True)
            time.sleep(2.0)

        # จังหวะที่ 3: เฉลย April Fool's
        main_container.empty()
        with main_container.container():
            st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
            st.markdown('<div class="main-title" style="color:#FF69B4;">SURPRISE! ✨</div>', unsafe_allow_html=True)
            st.markdown('<div class="gif-container"><img src="https://media.giphy.com/media/ZFzmkEqVFpVz02RU3j/giphy.gif"></div>', unsafe_allow_html=True)
            
            # เอฟเฟกต์พิมพ์ดีด
            msg_area = st.empty()
            full_text = "Happy April Fool's Dayคับน้ำอิง 😏"
            current_msg = ""
            for char in full_text:
                current_msg += char
                msg_area.markdown(f'<div style="font-size: 38px; font-weight: 900; color: #FFEA20; text-shadow: 3px 3px #000;">{current_msg}</div>', unsafe_allow_html=True)
                time.sleep(0.07)

            st.markdown('<div style="font-size: 22px; color: #fff; margin-top: 15px; font-weight:bold; background:rgba(0,0,0,0.3); border-radius:20px; padding:15px;">ตั๋วโดนคนเจียงใหม่วอกแล้วน้ำอิง สมน้ำหน้า🤪</div>', unsafe_allow_html=True)
            st.balloons()
            st.snow()
            st.markdown('<div style="color: #ccc; font-style: italic; margin-top: 50px;">(โคตรจะเริ่ดเลยล่ะ 😜)</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
