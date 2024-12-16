import argparse
import tkinter as tk

def validate_input(val) -> bool:
    return val == "" or (val.isdigit() and 1 <= int(val) <= 9)

def on_change(entries, solve_button):
    puzzle_input = [[entry.get() or "0" for entry in row] for row in entries]
    if validate_puzzle(puzzle_input):
        solve_button.config(state=tk.NORMAL, text="Solve")  # Enable solve button if valid
    else:
        solve_button.config(state=tk.DISABLED, text="Invalid Puzzle")  # Disable solve button if invalid

def get_gui_input():
    window = tk.Tk()
    window.title("Sudoku Solver")
    window.geometry("600x600")
    window.resizable(width=False, height=False)
    window.configure(padx=20, pady=20, background='#ffc300')

    for i in range(12):
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(i, weight=1)

    entry_padding = 3
    canvas_height = 478
    canvas_width = 560
    vline = canvas_width/9
    hline = canvas_height/9
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='#ffc86c')
    canvas.place(x=0, y=0)

    for i in range(1, 9):
        if i % 3 == 0:
            # Thick vertical line
            canvas.create_line(i * vline, 0, i * vline, canvas_height+entry_padding, width=3, fill='#6d3b2c') 
            # Thick horizontal line
            canvas.create_line(0, i * hline, canvas_width+entry_padding, i * hline, width=3, fill='#6d3b2c')
        else:
            # Thin vertical line
            canvas.create_line(i * vline, 0, i * vline, canvas_height+entry_padding, width=1, fill='#6d3b2c')  
            # Thin horizontal line
            canvas.create_line(0, i * hline, canvas_width+entry_padding, i * hline, width=1, fill='#6d3b2c')

    entries = []
    for row in range(9):
        puzzle_row = []
        for col in range(9):
            entry = tk.Entry(window, relief='flat', bg='#ffc86c', fg='black', highlightthickness='0', font=('Arial', 18), justify='center', validate="key", vcmd=(window.register(validate_input), '%P'))
            entry.grid(row=row, column=col, sticky='NSEW', padx=entry_padding, pady=entry_padding)
            entry.insert(0, tk.END)
            puzzle_row.append(entry)
        entries.append(puzzle_row)

    clear_button = tk.Button(window, text="Clear", font=('Arial', 18), command=lambda: [[entry.delete(0, tk.END) for entry in row] for row in entries])
    solve_button = tk.Button(window, text="Invalid Puzzle", font=('Arial', 18), state=tk.DISABLED, command=lambda: handle_puzzle([[entry.get() or "0" for entry in row] for row in entries], entries=entries))
    quit_button = tk.Button(window, text="Quit", font=('Arial', 18), command=window.destroy)
    
    clear_button.grid(row=10, column=0, columnspan=3, sticky='NSEW', padx=5)
    solve_button.grid(row=10, column=3, columnspan=3, sticky='NSEW', padx=5)
    quit_button.grid(row=10, column=6, columnspan=3, sticky='NSEW', padx=5)

    for row in entries:
        for entry in row:
            entry.bind("<KeyRelease>", lambda change_event, entries=entries, solve_button=solve_button: on_change(entries, solve_button))

    window.mainloop()


def get_input() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="81 digit string representing a sudoku puzzle", dest="puzzle_data", type=str)
    args = parser.parse_args()
    try:
        input = args.puzzle_data
        if input is None:
            input = get_gui_input()
            exit(1)
            raise NotImplementedError
        if len(input) != 81:
            raise SyntaxError
        if not input.isdigit():
            raise ValueError
        return input
    except SyntaxError:
        print("Invalid PUZZLE_DATA. Must be exactly 81 characters in length")
        exit(1)
    except ValueError:
        print("Invalid PUZZLE_DATA. Puzzle can only contain digits 1-9")
        exit(1)

def parse_input(puzzle_data: str) -> list[list[str]]:
    puzzle = [list(puzzle_data[i:i+9]) for i in range(0, len(puzzle_data), 9)]
    return puzzle

def find_next_empty_cell(puzzle: list[list[str]]) -> list[int]:
    for r in range(0, len(puzzle)):
        for c in range(0, len(puzzle[r])):
            if puzzle[r][c] == '0':
                return [r,c]
    return [-1, -1]

def check_square(puzzle: list[list[str]], r: int, c: int, num: int) -> bool:
    if puzzle[r].count(str(num)) > 0:
        return False
    if [row[c] for row in puzzle].count(str(num)):
        return False
    for i in range(3):
        for j in range(3):
            if puzzle[i+((r//3)*3)][j+((c//3)*3)] == str(num):
                return False
    return True

def validate_puzzle(puzzle: list[list[str]]) -> bool:
    for r in range(0, len(puzzle)):
        for c in range(0, len(puzzle[r])):
            if puzzle[r][c] != '0':
                n = puzzle[r][c]
                puzzle[r][c] = '0'
                if not check_square(puzzle, r, c, n):
                    return False
                puzzle[r][c] = n
    return True

def solve(puzzle) -> bool:
    pos = find_next_empty_cell(puzzle)
    if pos == [-1, -1]:
        return True
    row, col = pos[0], pos[1]
    for num in range(1, 10):
        if check_square(puzzle, row, col, num):
            puzzle[row][col] = str(num)
            if solve(puzzle):
                return True
            puzzle[row][col] = '0'
    return False

def print_puzzle(puzzle) -> None:
    for r in puzzle:
        for c in r:
            print(c, end=' ')
        print()

def handle_puzzle(puzzle, entries=None) -> None:
    if not validate_puzzle(puzzle):
        print("Invalid puzzle")
        exit(1)
    if solve(puzzle):
        if entries:
            for r in range(9):
                for c in range(9):
                    entries[r][c].delete(0, tk.END)
                    entries[r][c].insert(0, puzzle[r][c])
        else:
            print_puzzle(puzzle)
    else:
        print("No solution exists")
        exit(1)

def main() -> None:
    input = get_input()
    puzzle = parse_input(input)
    handle_puzzle(puzzle)


if __name__ == "__main__":
    main()

# Sample: 530070000600195000098000060800060003400803001700020006060000280000419000000080079