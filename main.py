import sys

def get_input():
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

def main():
    input = get_input()
    print(input)


if __name__ == "__main__":
    main()
