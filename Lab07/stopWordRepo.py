# Author: Perfect Makuwerere
# Date: March 9, 2026
# Description: Manages a persistent repository of stopwords using pickling.

import os
import pickle

STOPWORD_FILE = "stopwordset.data" 

def readStopWordsFile(stop_set):
    filename = input("Please enter the name of the new stopwords file: ")
    while not os.path.exists(filename):
        filename = input("File not found. Enter name: ")
    
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            if word in stop_set:
                print(f"We already have the word: {word}") 
            else:
                stop_set.add(word)

def writeStopWordsFile(stop_set):
    filename = input("Please enter the name of the stopwords file to write to: ")
    with open(filename, 'w') as file:
        for word in sorted(stop_set):
            file.write(word + "\n") 

def displayStopWords(stop_set):
    print(f"Currently we have {len(stop_set)} stopwords:")
    for word in stop_set:
        print(word)

def storeStopWords(stop_set):
    with open(STOPWORD_FILE, 'wb') as file: 
        pickle.dump(stop_set, file) 

def restoreStopWords():
    with open(STOPWORD_FILE, 'rb') as file: 
        return pickle.load(file) 
def main():
    if os.path.exists(STOPWORD_FILE):
        stopwords = restoreStopWords() 
    else:
        stopwords = set() 

    print("Welcome to the stopword repository!")
    choice = ""
    while choice != "4":
        print("\n1. Add a new list of stopwords\n2. Write current set to a file")
        print("3. Display current set\n4. Quit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            readStopWordsFile(stopwords)
        elif choice == "2":
            writeStopWordsFile(stopwords)
        elif choice == "3":
            displayStopWords(stopwords)
    
    storeStopWords(stopwords) 
    print("Thank you for using the stopword repository!")

if __name__ == "__main__":
    main()