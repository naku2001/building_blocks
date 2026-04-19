# Author: Perfect-Princess Makuwerere
# Date: April 19, 2026
# Description: Uses recursion and a global count to check if parentheses are balanced.

# Global variable to track balance [cite: 90]
count = 0

def parenTest(line, position):
    """
    Recursive check for balanced parentheses.
    :param line: The string of parentheses
    :type line: str
    :param position: Current index in the string
    :type position: int
    :return: True if balanced, False otherwise
    """
    global count
    
    # Base Case: Reached the end of the string [cite: 93]
    if position == len(line):
        return count == 0  # Balanced if count is back to zero [cite: 96]

    # Update count based on current character [cite: 97]
    if line[position] == '(':
        count += 1
    elif line[position] == ')':
        count -= 1
        
    # Condition: A ')' must never come before a matching '(' [cite: 96]
    if count < 0:
        return False
        
    # Recursive step: Move to the next position [cite: 98, 99]
    return parenTest(line, position + 1)

def main():
    global count
    # Reset count in case of multiple runs
    count = 0
    
    # Prompt the user [cite: 101]
    user_input = input("Please enter a series of parenthesis to see if they are balanced: ")
    
    # Initial call with position 0 [cite: 102]
    if parenTest(user_input, 0):
        print(f"{user_input} is balanced.")
    else:
        print(f"{user_input} is not balanced.")

if __name__ == "__main__":
    main()