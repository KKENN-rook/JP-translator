import unittest
from unittest.mock import patch
from src.jp_translator.clipboard import get_clipboard


class TestClipboardFuncs(unittest.TestCase):

    @patch('src.jp_translator.clipboard.pyperclip.paste')
    def test_get_clipboard(self, mock_paste):
        mock_paste.return_value = "Random clipboard content."
        result = get_clipboard()
        self.assertEqual(result, "Random clipboard content.")


if __name__ == '__main__':
    unittest.main()