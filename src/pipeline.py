import argparse

from wordsearch import generate_wordsearch, save_wordsearch
from clue_generator import generate_clues

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--words", required=True, help="Path to word list file")
    parser.add_argument("--mode", choices=["wordsearch"], default="wordsearch")
    args = parser.parse_args()

    with open(args.words, "r") as f:
        words = [line.strip() for line in f if line.strip()]

    if args.mode == "wordsearch":
        grid = generate_wordsearch(words)
        path = save_wordsearch(grid)
        print(f"✅ Word search puzzle saved at {path}")

    # Generate clues
    clues = generate_clues(words)
    print("\n📝 Clues:")
    for w, c in clues.items():
        print(f"{w}: {c}")
