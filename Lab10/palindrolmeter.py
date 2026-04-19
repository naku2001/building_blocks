# Author: Perfect-Princess Makuwerere
# Date: April 19, 2026
# Description: Checks if a word is a palindrome using an iterative loop.

def palinTest(word):
    """
    Iterative test for palindrome.
    :param word: The string to test
    :type word: str
    :return: True if palindrome, False otherwise
    """
    # Using a loop to compare characters from both ends [cite: 51, 52]
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False  # Characters do not match [cite: 53]
    return True  # All characters matched [cite: 53]

def main():
    # Prompt user for word [cite: 55]
    user_word = input("Please enter a word to test if it is a palindrome: ")
    
    # Check and output message [cite: 56]
    if palinTest(user_word):
        print(f"{user_word} is a palindrome!")
    else:
        print(f"{user_word} is not a palindrome.")

if __name__ == "__main__":
    main()