import unittest
from src.jp_translator.translator import is_japanese


class TestTranslatorFuncs(unittest.TestCase):

    def test_isjapanese_hiragana(self):
        self.assertTrue(is_japanese("こんにちは"))

    def test_isjapanese_katakana(self):
        self.assertTrue(is_japanese("ホットドッグ"))

    def test3_isjapanese_kanji(self):
        self.assertTrue(is_japanese("世界"))

    def test4_isjapanese_mixedcharacters(self):
        self.assertTrue(is_japanese("こんにちはホットドッグ世界"))


if __name__ == '__main__':
    unittest.main()