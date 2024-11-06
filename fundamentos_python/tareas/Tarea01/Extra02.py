"""
    Determines if a word/sentence is a palindrome ignoring spaces, punctuation, and capitalization

    Args:
        text (str): The word/sentence to evaluate

    Returns:
        bool: True if the word/sentence is a palindrome, False otherwise
"""
def is_palindrome(text: str) -> bool:
    l: int = 0
    r: int = len(text) - 1
    while l < r:
        if not text[l].isalnum():
            l += 1
        elif not text[r].isalnum():
            r -= 1
        elif text[l].lower() != text[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True

"""
    Main function
"""
def main() -> None:
    text: str = input('Enter a word/sentence: ')
    print(is_palindrome(text) and 'Is palindrome' or 'Is not palindrome')

"""
    Entry point
"""
if __name__ == '__main__':
    try:
        main()
    except EOFError: # Ctrl + D
        print('Bye')
    except KeyboardInterrupt: # Ctrl + C
        print('Bye')