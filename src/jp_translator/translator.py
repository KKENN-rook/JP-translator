import re
from functools import lru_cache

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


@lru_cache(maxsize=32)
def translate_text(text: str) -> str:
    """
    Translates Japanese input to English.

    Args:
        text (str): Japanese text to translate

    Returns:
        str: text translated to english or input txt if translation is invalid.
    """
    try:
        if is_japanese(text):
            # TODO
            return None
        else:
            raise ValueError("The text does not contain Japanese characters!")
    except ValueError as ve:
        return f"Value error: {str(ve)}"
    except Exception as e:
        # Debugging statement
        print(f"An error has occurred: {e}")
        return "Error: An unexpected error has occurred during translation."


def print_cache_stats():
    """
    Prints cache statistics (Debugging)
    """
    cache_stats = translate_text.cache_info()
    print(cache_stats)


print(translate_text("こんにちはホットドッグ世界"))