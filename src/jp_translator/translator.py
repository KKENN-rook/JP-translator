import re

HIRAGANA_RE = re.compile(r'[\u3040-\u309F]')
KATAKANA_RE = re.compile(r'[\u30A0-\u30FF]')
KANJI_RE = re.compile(r'[\u4E00-\u9FFF]')


def is_japanese(text: str) -> bool:
    """
    Checks if the input text is Japanese.
    Determined by the presence of Hiragana, Katakana, or Kanji.

    Args:
        text (str): str to check

    Returns:
        boolean: True if the text contains JP chars, else False
    """
    return bool(HIRAGANA_RE.search(text) or KATAKANA_RE.search(text)
                or KANJI_RE.search(text))
