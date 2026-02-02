import numpy as np

def get_matrix(name):  # taking matrix values from user
    while True:
        try:
            rows = int(input(f"Enter number of rows for Matrix {name}: "))
            cols = int(input(f"Enter number of columns for Matrix {name}: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive numbers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

    print(f"\nEnter values for Matrix {name} row-wise (space separated):")
    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) == cols:
                    matrix.append(row)
                    break
                else:
                    print(f"Please enter exactly {cols} values.")
            except ValueError:
                print("Invalid input. Please enter numeric values only.")

    return np.array(matrix)


def print_matrix(M, title):
    print(f"\n{title}")
    for row in M:
        print(row)


def analyze_matrix(M, name):  # Analyzing the matrix
    rows, cols = M.shape
    print(f"\n--- Analysis of Matrix {name} ---")

    print("• Square Matrix" if rows == cols else "• Rectangular Matrix")
    if rows == 1:
        print("• Row Matrix")
    if cols == 1:
        print("• Column Matrix")
    if np.all(M == 0):
        print("• Zero Matrix")

    if rows == cols:
        if np.allclose(M, np.diag(np.diag(M))):
            print("• Diagonal Matrix")
            if np.all(M.diagonal() == M.diagonal()[0]):
                print("• Scalar Matrix")
        if np.allclose(M, np.eye(rows)):
            print("• Identity Matrix")
        if np.allclose(M, M.T):
            print("• Symmetric Matrix")
        if np.allclose(M, -M.T):
            print("• Skew-Symmetric Matrix")

def determinant_matrix(M, name):  # to find determinant of matrix
    if M.shape[0] != M.shape[1]:
        print(f"\nDeterminant not possible for Matrix {name} (not square).")
        return
    det = np.linalg.det(M)
    print(f"\nDeterminant of Matrix {name}: {det:.2f}")



def main():
    A = get_matrix("A")
    B = get_matrix("B")

    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")

    while True:        # matrix tasks to be performed

        print("\n--- Matrix Operations Menu ---")
        print("1. Matrix Analysis")
        print("2. Addition")
        print("3. Subtraction")
        print("4. Multiplication")
        print("5. Transpose")
        print("6. Determinant")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            m = input("Analyze which matrix? (A/B): ").upper()
            if m == "A":
                analyze_matrix(A, "A")
            elif m == "B":
                analyze_matrix(B, "B")
            else:
                print("Invalid choice.")

        elif choice == "2":
            if A.shape == B.shape:
                print_matrix(A + B, "A + B")
            else:
                print("Addition not possible (different dimensions).")

        elif choice == "3":
            if A.shape == B.shape:
                print_matrix(A - B, "A - B")
            else:
                print("Subtraction not possible (different dimensions).")

        elif choice == "4":
            if A.shape[1] == B.shape[0]:
                print_matrix(A @ B, "A × B")
            else:
                print("Multiplication not possible (columns of A ≠ rows of B).")

        elif choice == "5":
            m = input("Transpose which matrix? (A/B): ").upper()
            if m == "A":
                print_matrix(A.T, "Transpose of Matrix A")
            elif m == "B":
                print_matrix(B.T, "Transpose of Matrix B")
            else:
                print("Invalid choice.")

        elif choice == "6":
            m = input("Determinant of which matrix? (A/B): ").upper()
            if m == "A":
                determinant_matrix(A, "A")
            elif m == "B":
                determinant_matrix(B, "B")
            else:
                print("Invalid choice.")

        elif choice == "7":
            print("Program Exit.")
            break

        else:
            print("Invalid choice.")
            continue

        if input("\nDo you want to continue? (Y/N): ").upper() != "Y":
            print("Thank you for using the Matrix Operations Tool.")
            break


if __name__ == "__main__":
    main()
    