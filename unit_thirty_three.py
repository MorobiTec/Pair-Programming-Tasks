#pop quiz

# Check if a number is a perfect square 
def is_perfect_square(n):
    if n < 0:
        return False
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return x * x == n

# Calculate the numeric value for a word based on the current mapping
def word_value(word, mapping):
    return int(''.join(str(mapping[char]) for char in word))

# Check if the sum of digits of a number is a perfect square
def sum_of_digits_is_square(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return is_perfect_square(digit_sum)

# Backtracking function to assign digits to letters
def solve_puzzle(words, mapping, used_digits):
    if len(mapping) == len(set(''.join(words))):  # All letters are assigned
        for word in words:
            value = word_value(word, mapping)
            if not (is_perfect_square(value) and sum_of_digits_is_square(value)):
                return False
        return True

    # Get the next letter to assign
    for letter in set(''.join(words)):
        if letter not in mapping:
            break

    # Try each digit for this letter
    for digit in range(10):
        if digit not in used_digits:
            mapping[letter] = digit
            used_digits.add(digit)

            # Recursive call to continue with the next letter
            if solve_puzzle(words, mapping, used_digits):
                return True

            # Backtrack
            del mapping[letter]
            used_digits.remove(digit)

    return False

# Main function to setup the problem and find the solution
def main():
    words = ["A", "MERRY", "XMAS", "TO", "ALL"]
    
    # Pre-assign the known values
    initial_mapping = {'T': 8, 'O': 1}
    used_digits = set(initial_mapping.values())

    # Solve the puzzle
    if solve_puzzle(words, initial_mapping, used_digits):
        print("Solution found:")
        for letter, digit in sorted(initial_mapping.items()):
            print(f"{letter} = {digit}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
