import unittest
from unittest.mock import patch
from src.jp_translator.translator import is_japanese, translate_text


class TestTranslatorFuncs(unittest.TestCase):

    def test_isjapanese_hiragana(self):
        self.assertTrue(is_japanese("こんにちは"))

    def test_isjapanese_katakana(self):
        self.assertTrue(is_japanese("ホットドッグ"))

    def test_isjapanese_kanji(self):
        self.assertTrue(is_japanese("世界"))

    def test_isjapanese_mixedjpchars(self):
        self.assertTrue(is_japanese("こんにちはホットドッグ世界"))

    def test_isjapanese_nonjp(self):
        self.assertFalse(is_japanese("Hello world"))

    def test_isjapanese_emptystr(self):
        self.assertFalse(is_japanese(""))

    @patch('src.jp_translator.translator.translator.translate_text')
    def test_translate_shortphrase(self, mock_translate):
        # Mock the API response
        mock_translate.return_value.text = "Hello Hot Dog World"

        result = translate_text("こんにちはホットドッグ世界")
        self.assertEqual(result, "Hello Hot Dog World")

    @patch('src.jp_translator.translator.translator.translate_text')
    def test_cache_functionality(self, mock_translate):
        mock_translate.return_value.text = "Hello"

        # First call, uses API
        result1 = translate_text("こんにちは")
        self.assertEqual(result1, "Hello")

        # Second call, uses cache
        result2 = translate_text("こんにちは")
        self.assertEqual(result2, "Hello")
        mock_translate.assert_called_once_with(
            "こんにちは",
            target_lang='EN-US'
        )


if __name__ == '__main__':
    unittest.main()
