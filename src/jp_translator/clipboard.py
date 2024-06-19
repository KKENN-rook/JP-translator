import pyperclip


def get_clipboard():
    """
    Returns the current text content of the sys clipboard
    """
    return pyperclip.paste().strip()
