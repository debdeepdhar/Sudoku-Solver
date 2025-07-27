import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = tk.Entry(
                    self.root, width=3, font=('Arial', 16),
                    justify='center', bg='white'
                )
                cell.grid(row=i, column=j, padx=1, pady=1)
                row.append(cell)
            self.cells.append(row)

        solve_btn = tk.Button(
            self.root, text="Solve", command=self.solve,
            font=('Arial', 12), bg='lightgreen'
        )
        solve_btn.grid(row=9, column=4, pady=10)

        clear_btn = tk.Button(
            self.root, text="Clear", command=self.clear,
            font=('Arial', 12), bg='lightcoral'
        )
        clear_btn.grid(row=9, column=3, pady=10)

    def solve(self):
        # Get user input
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                if value.isdigit() and 1 <= int(value) <= 9:
                    self.board[i][j] = int(value)
                else:
                    self.board[i][j] = 0

        # Solve Sudoku
        if solve_sudoku(self.board):
            # Update GUI with solution
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(self.board[i][j]))
        else:
            messagebox.showerror("Error", "No solution exists!")

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.board[i][j] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()