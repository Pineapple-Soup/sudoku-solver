import sys

def get_input() -> str:
    try:
        input = sys.argv[1]
        if len(input) != 81:
            raise SyntaxError
        if not input.isdigit():
            raise ValueError
        return input
    except IndexError:
        print("Usage: solve.py PUZZLE_DATA")
        exit(1)
    except SyntaxError:
        print("Invalid PUZZLE_DATA. Must be 81 Characters in length")
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
    if puzzle[r].count(num):
        return False
    if [row[c] for row in puzzle].count(num):
        return False
    for i in range(3):
        for j in range(3):
            if puzzle[i+((r//3)*3)][j+((c//3)*3)] == num:
                return False
    return True

def main() -> None:
    input = get_input()
    print(input)
    puzzle = parse_input(input)
    print(find_next_empty_cell(puzzle))


if __name__ == "__main__":
    main()
