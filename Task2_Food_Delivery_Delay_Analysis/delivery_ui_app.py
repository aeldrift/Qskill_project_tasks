import streamlit as st
import io
import sys
import runpy


# PAGE CONFIG
st.set_page_config(
    page_title="Food Delivery Delay Analysis",
    page_icon="🍔",
    layout="centered"
)

# CUSTOM CSS 
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8fafc, #ecfeff);
}
h1, h2, h3 {
    color: #0f172a;
    font-weight: 700;
}
.stButton>button {
    background: linear-gradient(90deg, #0ea5e9, #22d3ee);
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-size: 16px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #0284c7, #0ea5e9);
}
.stCodeBlock {
    background-color: #020617;
    color: #22c55e;
    border-radius: 12px;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

#  HEADER
st.markdown("""
<div style="text-align:center; padding:1.5rem 0;">
    <h1>🍔 Food Delivery Delay Analysis</h1>
    <p style="color:#334155; font-size:1.1rem;">
        Exploratory Data Analysis using Pandas & Matplotlib <br>
        The task is working with a fixed dataset, so the UI is designed as a wrapper.
If needed, it can easily be extended to accept file uploads.
    </p>
</div>
""", unsafe_allow_html=True)

#  SIDEBAR
with st.sidebar:
    st.markdown("## 📘 About")
    st.write("""
    This project analyzes food delivery delays
    based on vehicle type and order category.
    """)

    st.markdown("## 🚀 Features")
    st.write("""
    - Dataset inspection  
    - Data cleaning  
    - Delivery time analysis  
    - Delay categorization  
    - Visual insights  
    """)

    st.markdown("## 💡 Skills Demonstrated")
    st.write("""
    - Python  
    - Pandas  
    - Matplotlib  
    - Exploratory Data Analysis  
    - AI-Assisted Development (ChatGPT)  
    """)

#  ACTION 
st.divider()
st.subheader("▶️ Run Analysis")

run_analysis = st.button("🚀 Execute Analysis")

# EXECUTION 
if run_analysis:
    st.markdown("### 📤 Console Output")

    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        # Run the LOCKED script as-is
        runpy.run_path("task2_food_delivery_analysis.py")
    finally:
        sys.stdout = sys.__stdout__

    st.code(buffer.getvalue(), language="text")

    st.markdown("### 📊 Visualizations")
    st.info("All plots generated below are produced directly from the original analysis code.")

#  FOOTER
st.markdown("""
<hr>
<div style="text-align:center; color:#64748b;">
 • Task 2 (Food Delivery Delay Analysis)
</div>
""", unsafe_allow_html=True)
