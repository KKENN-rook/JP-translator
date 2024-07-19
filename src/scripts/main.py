import time
from src.jp_translator.clipboard import get_clipboard
from src.jp_translator.translator import translate_text
from src.dictionary.jmdict_parser import JMDictParser


def main():
    # Initial variables
    parser = JMDictParser()
    prev_txt = None

    while True:
        # Program intialization
        print("\nWelcome to the Japanese Translator/Dictionary!")
        print("1. Translation Mode")
        print("2. Dictionary Mode")
        print("3. Exit")
        choice = input("Please choose a mode (1/2/3): ")
        if choice == '1':
            mode = 'translation'
            print("Translation mode selected."
                  " Copy Japanese text to the clipboard.")
        elif choice == '2':
            mode = 'dictionary'
            print("Dictionary mode selected."
                  "Copy a Japanese term to the clipboard.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            return
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        # Translation loop
        while True:
            clipboard_txt = get_clipboard()
            if clipboard_txt != prev_txt:
                prev_txt = clipboard_txt
                if mode == 'translation':
                    translation = translate_text(clipboard_txt)
                    print(f"Clipped Text: {clipboard_txt}")
                    print(f"Translation: {translation}")
                elif mode == 'dictionary':
                    result = parser.lookup(clipboard_txt)
                    if result:
                        print(f"Your query: {clipboard_txt}")
                        print("Dictionary Lookup Result:")
                        print(f"Kanji: {result.get('kanji', 'N/A')}")
                        print(f"Readings: {result.get('readings', 'N/A')}")
                        print(f"Eng: {result.get('glosses', 'N/A')}")
                    else:
                        print("No entry found. Invalid query.")

            # Wait before checking for clipboard changes
            time.sleep(3)

            # Prompt user for feature switch
            # Temporary solution until GUI is implemented 
            user_input = input("\n Press 'm' to switch modes or 'q' to quit: "
                               "Or any other key to continue.").lower()
            if user_input == 'm':
                break
            elif user_input == 'q':
                print("Exiting the program. Goodbye!")
                return
            else:
                continue


if __name__ == "__main__":
    main()
