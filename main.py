from stats import report_character_count
import sys

def main():
    # try:
    #     path_book = sys.argv[1]
    # except Exception:
    #     print("Usage: python3 main.py <path_to_book>")
    #     sys.exit(1)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_book = sys.argv[1]
    

    report_character_count(path_book)



main()
