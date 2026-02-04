import streamlit as st
import numpy as np
import io
import sys

#  IMPORT YOUR LOCKED FILE (name must match)
import matrix_operations_tool as mot


st.set_page_config(
    page_title="Matrix Operations Tool",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Matrix Operations Tool")
st.caption("Streamlit UI built on top of locked CLI logic")

# MATRIX INPUT 
def matrix_input(name):
    st.subheader(f"Matrix {name}")

    rows = st.number_input(
        f"Enter number of rows for Matrix {name}",
        min_value=1, max_value=10, value=3, key=f"{name}_r"
    )

    cols = st.number_input(
        f"Enter number of columns for Matrix {name}",
        min_value=1, max_value=10, value=3, key=f"{name}_c"
    )

    data = []
    for i in range(rows):
        data.append(
            st.text_input(
                f"Row {i+1} (space separated)",
                key=f"{name}_row_{i}"
            )
        )

    # validation
    if any(d.strip() == "" for d in data):
        return None

    try:
        matrix = np.array([list(map(float, r.split())) for r in data])
        if matrix.shape == (rows, cols):
            return matrix
    except:
        return None

    return None


A = matrix_input("A")
B = matrix_input("B")

if A is None or B is None:
    st.info("⬆️ Enter complete values for both matrices to continue")
    st.stop()

st.success("Matrices loaded successfully")

st.write("### Matrix A")
st.write(A)

st.write("### Matrix B")
st.write(B)

# MENU
st.divider()
st.subheader("Matrix Operations Menu")

choice = st.selectbox(
    "Select Operation",
    [
        "Matrix Analysis",
        "Addition",
        "Subtraction",
        "Multiplication",
        "Transpose",
        "Determinant"
    ]
)

# EXECUTION 
if st.button("Execute"):

    # Capture printed output
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        if choice == "Matrix Analysis":
            m = st.radio("Analyze which matrix?", ["A", "B"])
            if m == "A":
                mot.analyze_matrix(A, "A")
            else:
                mot.analyze_matrix(B, "B")

        elif choice == "Addition":
            if A.shape == B.shape:
                mot.print_matrix(A + B, "A + B")
            else:
                print("Addition not possible (different dimensions).")

        elif choice == "Subtraction":
            if A.shape == B.shape:
                mot.print_matrix(A - B, "A - B")
            else:
                print("Subtraction not possible (different dimensions).")

        elif choice == "Multiplication":
            if A.shape[1] == B.shape[0]:
                mot.print_matrix(A @ B, "A × B")
            else:
                print("Multiplication not possible (columns of A ≠ rows of B).")

        elif choice == "Transpose":
            m = st.radio("Transpose which matrix?", ["A", "B"])
            if m == "A":
                mot.print_matrix(A.T, "Transpose of Matrix A")
            else:
                mot.print_matrix(B.T, "Transpose of Matrix B")

        elif choice == "Determinant":
            m = st.radio("Determinant of which matrix?", ["A", "B"])
            if m == "A":
                mot.determinant_matrix(A, "A")
            else:
                mot.determinant_matrix(B, "B")

    finally:
        sys.stdout = sys.__stdout__

    output = buffer.getvalue()
    st.code(output)
