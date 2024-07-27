import tkinter as tk
from tkinter import ttk
from src.jp_translator.clipboard import get_clipboard
from src.jp_translator.translator import translate_text
from src.dictionary.jmdict_parser import JMDictParser
from threading import Thread
import time


class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Japanese Translator/Dictionary")
        self.geometry("600x400")

        self.mode = tk.StringVar(value="translation")
        self.dictionary = JMDictParser()
        self.prev_txt = None
        self.running = True

        self.create_widgets()
        self.check_clipboard_thread()

    def create_widgets(self):
        # Main window frame
        mainframe = ttk.Frame(self, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))
        # Allow mainframe to expand to fill extra space if resized
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Mode selection buttons
        mode_frame = ttk.Frame(mainframe)
        mode_frame.grid(column=0, row=0, pady=10, sticky=(tk.W, tk.E))
        trans_button = ttk.Button(mode_frame, text="Translation Mode", command=self.set_translation_mode)
        trans_button.grid(column=0, row=0)
        dict_button = ttk.Button(mode_frame, text="Dictionary Mode", command=self.set_dictionary_mode)
        dict_button.grid(column=1, row=0)
        quit_button = ttk.Button(mode_frame, text="Quit", command=self.quit)
        quit_button.grid(column=2, row=0)

        # Formats mode_frame widgets
        for child in mode_frame.winfo_children():
            child.grid_configure(padx=10)

        # Result display textbox
        self.result_text = tk.Text(mainframe, wrap="word", height=20, width=70)
        self.result_text.grid(column=0, row=1, pady=10, sticky=(tk.N, tk.E, tk.S, tk.W))

        # Configure grid weight for the widgets(textbox) inside the mainframe
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(1, weight=1)

    def add_separator(self):
        # Adds a dashed line separator
        self.result_text.insert(tk.END, "\n" + "-"*70 + "\n")

    def set_translation_mode(self):
        self.mode.set("translation")
        self.result_text.insert(tk.END, "Translation mode selected.\n")

    def set_dictionary_mode(self):
        self.mode.set("dictionary")
        self.result_text.insert(tk.END, "Dictionary mode selected.\n")

    def check_clipboard(self):
        while self.running:
            clipboard_txt = get_clipboard()
            if clipboard_txt != self.prev_txt:
                self.prev_txt = clipboard_txt
                if self.mode.get() == "translation":
                    translation = translate_text(clipboard_txt)
                    self.result_text.insert(tk.END, f"Clipped Text: {clipboard_txt}\nTranslation: {translation}\n")
                    self.add_separator()
                elif self.mode.get() == "dictionary":
                    result = self.dictionary.lookup(clipboard_txt)
                    if result:
                        self.result_text.insert(
                            tk.END,
                            f"Your query: {clipboard_txt}\n"
                            f"Dictionary Lookup Result:\n"
                            f"Kanji: {result.get('kanji', 'N/A')}\n"
                            f"Readings: {result.get('readings', 'N/A')}\n"
                            f"Eng: {result.get('glosses', 'N/A')}\n"
                        )
                    else:
                        self.result_text.insert(tk.END, "No entry found. Invalid query.\n")
                    self.add_separator()
            time.sleep(3)

    def check_clipboard_thread(self):
        thread = Thread(target=self.check_clipboard)
        thread.daemon = True
        thread.start()

    def quit(self):
        self.running = False
        self.destroy()


if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
