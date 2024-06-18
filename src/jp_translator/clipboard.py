import pyperclip


# Fetches system clipboard contents
def get_clipboard():
    return pyperclip.paste().strip()
