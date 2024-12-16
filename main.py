import tkinter as tk

# Function to create the empty Sudoku board with visually separated sections
def create_sudoku_board(root):
    # Create a frame to hold the Sudoku grid
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Create a canvas to draw the dividing lines
    canvas = tk.Canvas(root, width=324, height=324)  # 9 cells * 36px each
    canvas.grid(row=0, column=0, padx=10, pady=10)

    # Draw vertical and horizontal lines to separate the 3x3 sections
    for i in range(1, 9):
        if i % 3 == 0:  # Every 3 cells (i.e., at 3, 6, 9) we draw a thicker line
            canvas.create_line(i * 36, 0, i * 36, 324, width=3, fill="black")  # Vertical lines
            canvas.create_line(0, i * 36, 324, i * 36, width=3, fill="black")  # Horizontal lines
        else:
            canvas.create_line(i * 36, 0, i * 36, 324, width=1, fill="black")  # Vertical lines
            canvas.create_line(0, i * 36, 324, i * 36, width=1, fill="black")  # Horizontal lines

    # Create a 9x9 grid of Entry widgets on top of the canvas
    cells = []
    for row in range(9):
        row_cells = []
        for col in range(9):
            entry = tk.Entry(frame, width=3, font=('Arial', 18), justify='center', borderwidth=1, relief='solid')
            entry.grid(row=row, column=col, padx=0, pady=0, sticky="nsew")
            row_cells.append(entry)
        cells.append(row_cells)

    return cells, canvas

# Main function to set up the Tkinter window
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Sudoku Board")
    
    # Set the window size to 600x600
    root.geometry("600x600")

    # Configure the grid to make the frame expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create the empty Sudoku board with visual separation
    cells, canvas = create_sudoku_board(root)

    # Start the Tkinter event loop
    root.mainloop()

# Run the application
if __name__ == "__main__":
    main()
