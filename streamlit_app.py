import streamlit as st
import pandas as pd
from io import StringIO

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Data Splitter Tool", layout="wide")

st.title("🛠 เครื่องมือแยกข้อมูล Account")
st.subheader("วางข้อมูลที่คั่นด้วย | ลงในช่องด้านล่าง")

# ช่องสำหรับใส่ข้อมูล
raw_data = st.text_area("วางข้อมูลตรงนี้:", height=300, placeholder="example@hotmail.com|password123|token|id...")

if raw_data:
    try:
        # แยกข้อมูลรายบรรทัด
        lines = raw_data.strip().split('\n')
        processed_data = []

        for line in lines:
            if '|' in line:
                parts = line.split('|')
                processed_data.append(parts)

        # สร้าง DataFrame (ตาราง)
        # กำหนดชื่อคอลัมน์ (ปรับตามจำนวนข้อมูลที่พบ)
        max_cols = max(len(row) for row in processed_data)
        col_names = ["Email", "Password", "Token / Session", "UUID"] + [f"Extra_{i}" for i in range(max_cols - 4)]
        
        df = pd.DataFrame(processed_data, columns=col_names[:max_cols])

        # แสดงผลตาราง
        st.success(f"พบข้อมูลทั้งหมด {len(df)} รายการ")
        st.dataframe(df, use_container_width=True)

        # ปุ่มดาวน์โหลด
        csv = df.to_csv(index=False).encode('utf_8_sig')
        st.download_button(
            label="📥 ดาวน์โหลดเป็นไฟล์ Excel (CSV)",
            data=csv,
            file_name="split_data.csv",
            mime="text/csv",
        )

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการแยกข้อมูล: {e}")
else:
    st.info("รอรับข้อมูลจากคุณอยู่ครับ...")
