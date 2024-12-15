# sudoku-solver

This project provides a Sudoku Solver that can be run via the command line (CLI) or with a graphical user interface (GUI).
  <img width="594" alt="GUI Example" src="https://github.com/user-attachments/assets/d8143499-783a-494b-82ea-e28b4e019ec3" />

## Requirements
- Python 3.x

No additional dependencies are required

## Installation

Python 3.x is required for use. The GUI is built on the `tkinter` module, and the CLI leverages `argparse`, both of which should be installed by default with Python.
> [!TIP]
> If you don't have python installed, you can install it [here](https://www.python.org/downloads/)
1. Clone the repository or download the script
```bash
git clone https://github.com/Pineapple-Soup/sudoku-solver.git
```
2. Verify that you have Python 3.x installed by running:
```bash
python --version
```

## Usage
### Command Line Interface (CLI)
To use the Sudoku solver with command-line input, run the script with the -p flag followed by an 81-digit string representing the puzzle:
```bash
python3 sudoku_solver.py -p 530070000600195000098000060800060003400803001700020006060000280000419000000080079
```
The string should represent the Sudoku puzzle row by row, with `0` representing empty cells.

### Graphical User Interface (GUI)
To use the Sudoku solver with GUI:
1. Run the script without the -p flag
```bash
python3 sudoku_solver.py
```
2. A GUI will open with a 9x9 grid of entry fields where you can input the puzzle manually
3. After entering the puzzle, the "Solve" button will be enabled if the puzzle is valid. Press it to solve the puzzle. The "Solve" button will remain disabled for invalid puzzles.
4. Press the "Clear" button to clear the grid of all numbers
5. Press the "Quit" button to close the program.
