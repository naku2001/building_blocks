# Author: Perfect-Princess Makuwerere
# Date: April 19, 2026
# Description: Checks if a word is a palindrome using a recursive function.

def palinTest(word):
    """
    Recursive test for palindrome.
    :param word: The string to test
    :type word: str
    :return: True if palindrome, False otherwise
    """
    # Base case: empty string or single character [cite: 65, 75]
    if len(word) <= 1:
        return True
    
    # If first and last characters don't match, it's not a palindrome [cite: 66, 76]
    if word[0] != word[-1]:
        return False
    
    # Recursive step: call with a smaller version of the string [cite: 67, 77]
    return palinTest(word[1:-1])

def main():
    # Reuse the same main logic as the iterative version [cite: 78]
    user_word = input("Please enter a word to test if it is a palindrome: ")
    
    if palinTest(user_word):
        print(f"{user_word} is a palindrome!")
    else:
        print(f"{user_word} is not a palindrome!")

if __name__ == "__main__":
    main()