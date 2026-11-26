"""The Printer Finally Answers: write one printer comeback line."""

from pathlib import Path

LINE = "Thumping me does not clear Error 49; it just updates my thump count to 313."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 240
    assert "\n" not in text
    try:
        out = Path("/output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
    except OSError:
        Path("entry.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
