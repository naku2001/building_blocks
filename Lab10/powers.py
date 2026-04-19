# Author: Perfect-Princess Makuwerere
# Date: April 19, 2026
# Description: Calculates the result of a base value raised to an exponent recursively.

def powers(base, exponent):
    """
    Recursive function to calculate power.
    :param base: The base integer value
    :type base: int
    :param exponent: The exponent integer value
    :type exponent: int
    :return: The result of base raised to the exponent
    """
    # Print the current call for tracing [cite: 32]
    print(f"powers ({base}, {exponent})")
    
    # Base case: if exponent is 1, return base [cite: 34]
    if exponent == 1:
        return base
    
    # Recursive step: base * powers(base, exponent - 1) [cite: 34, 35]
    return base * powers(base, exponent - 1)

def main():
    # Prompt user for input [cite: 37, 38]
    user_base = int(input("Please enter the base value: "))
    user_exponent = int(input("Please enter the exponent value: "))
    
    # Call function and store result [cite: 39]
    result = powers(user_base, user_exponent)
    
    # Output the final result [cite: 40]
    print(f"{user_base}^{user_exponent} is {result}")

if __name__ == "__main__":
    main()