import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "site" / "py"))

FONT = str(Path(__file__).resolve().parent.parent / "site" / "fonts" / "JetBrainsMonoNerdFont-SemiBold.ttf")

from text2pdf import convert, wrap_lines


def test_wrap_splits_long_line():
    assert wrap_lines("a" * 170) == ["a" * 80, "a" * 80, "a" * 10]


def test_wrap_keeps_blank_lines():
    assert wrap_lines("a\n\nb") == ["a", "", "b"]


def test_wrap_normalizes_line_endings():
    assert wrap_lines("a\r\nb\rc") == ["a", "b", "c"]


def test_convert_returns_pdf():
    assert convert("hello", FONT).startswith(b"%PDF")


def test_convert_handles_empty_input():
    assert convert("", FONT).startswith(b"%PDF")