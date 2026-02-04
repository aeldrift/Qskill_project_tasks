import streamlit as st
import numpy as np
import io
import sys

import matrix_operations_tool as mot


# PAGE CONFIG 
st.set_page_config(
    page_title="Matrix Operations Tool",
    page_icon="🧮",
    layout="centered"
)

# CUSTOM CSS 
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
}

/* Headings */
h1, h2, h3 {
    color: #1f2937;
    font-weight: 700;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #4f46e5, #6366f1);
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-size: 16px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #4338ca, #4f46e5);
    transform: scale(1.02);
}

/* Inputs */
.stSelectbox, .stNumberInput, .stTextInput {
    background-color: white;
    border-radius: 8px;
}

/* Code output */
.stCodeBlock {
    background-color: #020617;
    color: #22c55e;
    border-radius: 12px;
    padding: 1rem;
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

#  HEADER 
st.markdown("""
<div style="text-align:center; padding:1.5rem 0;">
    <h1>🧮 Matrix Operations Tool</h1>
    <p style="color:#374151; font-size:1.1rem;">
        Interactive Matrix Calculator powered by NumPy & Streamlit
    </p>
</div>
""", unsafe_allow_html=True)

# SIDEBAR 
with st.sidebar:
    st.markdown("## 🧠 About")
    st.write("""
    This tool performs common matrix operations using **NumPy**
    with a clean **Streamlit UI**.
    """)
    st.markdown("## 🚀 Features")
    st.write("""
    - Matrix Analysis  
    - Addition / Subtraction  
    - Multiplication  
    - Transpose  
    - Determinant  
    """)
    st.markdown("## 💡 Skills Demonstrated")
    st.write("""
    - Python  
    - NumPy  
    - Streamlit UI  
    - Modular Code Design  
    - AI-Assisted Development (ChatGPT etc.)  
    
    """)

#  MATRIX INPUT 
def matrix_input(name):
    st.subheader(f"Matrix {name}")

    rows = st.number_input(
        f"Rows for Matrix {name}",
        min_value=1,
        max_value=10,
        value=3,
        key=f"{name}_rows"
    )

    cols = st.number_input(
        f"Columns for Matrix {name}",
        min_value=1,
        max_value=10,
        value=3,
        key=f"{name}_cols"
    )

    data = []
    for i in range(rows):
        data.append(
            st.text_input(
                f"Row {i+1} (space separated)",
                key=f"{name}_row_{i}"
            )
        )

    if any(d.strip() == "" for d in data):
        return None

    try:
        matrix = np.array([list(map(float, r.split())) for r in data])
        if matrix.shape == (rows, cols):
            return matrix
    except:
        return None

    return None


#  GET MATRICES 
A = matrix_input("A")
B = matrix_input("B")

if A is None or B is None:
    st.info("⬆️ Enter valid values for both matrices to continue")
    st.stop()

st.success("✅ Matrices loaded successfully")

st.write("### Matrix A")
st.dataframe(A, use_container_width=True)

st.write("### Matrix B")
st.dataframe(B, use_container_width=True)

#  MENU 
st.divider()
st.subheader("🔧 Matrix Operations Menu")

choice = st.selectbox(
    "Select Operation",
    [
        "📊 Matrix Analysis",
        "➕ Addition",
        "➖ Subtraction",
        "✖️ Multiplication",
        "🔁 Transpose",
        "🧮 Determinant"
    ]
)

selected_matrix = None
if choice in ["📊 Matrix Analysis", "🔁 Transpose", "🧮 Determinant"]:
    selected_matrix = st.radio(
        "Choose Matrix",
        ["A", "B"],
        horizontal=True
    )

execute = st.button("🚀 Execute")

#  EXECUTION 
if execute:
    with st.spinner("⏳ Computing result..."):
        buffer = io.StringIO()
        sys.stdout = buffer

        try:
            if choice == "📊 Matrix Analysis":
                mot.analyze_matrix(A, "A") if selected_matrix == "A" else mot.analyze_matrix(B, "B")

            elif choice == "➕ Addition":
                if A.shape == B.shape:
                    mot.print_matrix(A + B, "A + B")
                else:
                    print("Addition not possible (different dimensions).")

            elif choice == "➖ Subtraction":
                if A.shape == B.shape:
                    mot.print_matrix(A - B, "A - B")
                else:
                    print("Subtraction not possible (different dimensions).")

            elif choice == "✖️ Multiplication":
                if A.shape[1] == B.shape[0]:
                    mot.print_matrix(A @ B, "A × B")
                else:
                    print("Multiplication not possible (columns of A ≠ rows of B).")

            elif choice == "🔁 Transpose":
                mot.print_matrix(A.T, "Transpose of Matrix A") if selected_matrix == "A" else mot.print_matrix(B.T, "Transpose of Matrix B")

            elif choice == "🧮 Determinant":
                mot.determinant_matrix(A, "A") if selected_matrix == "A" else mot.determinant_matrix(B, "B")

        finally:
            sys.stdout = sys.__stdout__

    st.markdown("### 📤 Operation Output")
    st.code(buffer.getvalue(), language="text")

# FOOTER 
st.markdown("""
<hr>
<div style="text-align:center; color:#6b7280;">
    Built with ❤️ using Streamlit & NumPy 
</div>
""", unsafe_allow_html=True)
