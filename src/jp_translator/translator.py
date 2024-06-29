import re
import deepl
import os
from functools import lru_cache
from dotenv import load_dotenv


# Load API key
load_dotenv()
deepl_key = os.getenv('DEEPL_API_KEY')
if not deepl_key:
    raise ValueError('No API key found.')

# Initialize deepL translator
translator = deepl.Translator(deepl_key)

# Define regular expressions for Hiragana, Katakana, and Kanji (Unicode)
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
    Translates Japanese input to English using DeepL API
    Utilizes a LRU cache

    Args:
        text (str): Japanese text to translate

    Returns:
        str: text translated to english or input txt if translation is invalid.
    """
    try:
        if is_japanese(text):
            result = translator.translate_text(text, target_lang='EN-US')
            return result.text
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