import streamlit as st
import io
import sys
import runpy
import matplotlib.pyplot as plt


#  PAGE CONFIG 
st.set_page_config(
    page_title="Food Delivery Delay Analysis",
    page_icon="🍔",
    layout="centered"
)

#  CUSTOM CSS 
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

/* ===== Side carousel arrows ===== */
.side-arrow button {
    background: rgba(15, 23, 42, 0.85) !important;
    color: white !important;
    border-radius: 50% !important;
    width: 44px !important;
    height: 44px !important;
    font-size: 20px !important;
    padding: 0 !important;
    border: none !important;
}

.side-arrow button:hover {
    background: #0ea5e9 !important;
}
</style>
""", unsafe_allow_html=True)

# HEADER 
st.markdown("""
<div style="text-align:center; padding:1.5rem 0;">
    <h1>🍔 Food Delivery Delay Analysis</h1>
    <p style="color:#334155; font-size:1.05rem;">
        Exploratory Data Analysis using Pandas & Matplotlib
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
    - AI-Assisted Development (ChatGPT etc.)  
    """)

# ACTION 
st.divider()
st.subheader("▶️ Run Analysis")
st.markdown("The task is working with a fixed dataset, so the UI is designed as a wrapper, can't take file uploads.")

run_analysis = st.button("🚀 Execute Analysis")


#  EXECUTION 
if run_analysis:
    with st.spinner("⏳ Running analysis..."):
        buffer = io.StringIO()
        sys.stdout = buffer

        try:
            runpy.run_path("task2_food_delivery_analysis.py")
        finally:
            sys.stdout = sys.__stdout__

    st.session_state.console_output = buffer.getvalue()
    st.session_state.figures = [plt.figure(num) for num in plt.get_fignums()]
    plt.close("all")
    st.session_state.viz_index = 0

#  OUTPUT 
if "console_output" in st.session_state:

    # Console Output
    st.subheader("📄 Console Output")
    st.code(st.session_state.console_output, language="text")

    #  Visualizations 
    st.subheader("📊 Visualizations")
    st.info("All plots below are generated directly from the original analysis code.") 
    

    figures = st.session_state.figures
    total = len(figures)

    if total > 0:

        if "viz_index" not in st.session_state:
            st.session_state.viz_index = 0

        #  SIDE ARROWS & PLOT
        left, center, right = st.columns([1, 10, 1], vertical_alignment="center")

        with left:
            st.markdown('<div class="side-arrow">', unsafe_allow_html=True)
            if st.button("◀", key="prev"):
                if st.session_state.viz_index > 0:
                    st.session_state.viz_index -= 1
            st.markdown('</div>', unsafe_allow_html=True)

        with center:
            st.pyplot(figures[st.session_state.viz_index])
            st.markdown(
                f"""
                <div style="text-align:center; color:#475569; font-weight:600; margin-top:0.5rem;">
                    Slide {st.session_state.viz_index + 1} of {total}
                </div>
                """,
                unsafe_allow_html=True
            )

        with right:
            st.markdown('<div class="side-arrow">', unsafe_allow_html=True)
            if st.button("▶", key="next"):
                if st.session_state.viz_index < total - 1:
                    st.session_state.viz_index += 1
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("No plots were generated.")

#  FOOTER 
st.markdown("""
<hr>
<div style="text-align:center; color:#64748b;">
     • Task 2  (Food Delivery Delay Analysis)
</div>
""", unsafe_allow_html=True)
