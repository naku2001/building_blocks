# Author: Perfect Makuwerere
# Date: March 9, 2026
# Description: Performs term frequency analysis on a user-specified file.

import os

def readTextFile(word_dict):
    """
    Prompts for a file, reads it line by line, and counts word occurrences.
    :param word_dict: Dictionary to store word counts
    :type word_dict: dict
    """
    filename = input("Please enter the name of the file to analyze: ")
    while not os.path.exists(filename):
        print(f"{filename} does not exist!")
        filename = input("Please enter the name of the file to analyze: ")
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().lower() 
            words = line.split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1 
                else:
                    word_dict[word] = 1 

def outputFreq(word_dict):
    """
    Outputs the unique word count and each word with its frequency.
    :param word_dict: Dictionary containing word counts
    :type word_dict: dict
    """
    print(f"The file contained {len(word_dict)} unique words.") 
    for word, count in word_dict.items():
        print(f"{word}:{count}") 

def main():
    word_counts = {} 
    readTextFile(word_counts) 
    outputFreq(word_counts) 

if __name__ == "__main__":
    main()