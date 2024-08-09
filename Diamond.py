def print_diamond(letter):
    # Calculate the size of the diamond
    size = ord(letter) - ord('A') + 1
    diamond = []

    # Create the top half of the diamond (including the middle row)
    for i in range(size):
        row = [' '] * (2 * size - 1)  # Create a row filled with spaces
        row[size - i - 1] = chr(ord('A') + i)  # Place the letter on the left
        row[size + i - 1] = chr(ord('A') + i)  # Place the letter on the right
        diamond.append(''.join(row))  # Join the list into a string and add to the diamond

    # Mirror the top half to create the bottom half
    diamond += diamond[-2::-1]

    # Return the diamond as a string with newlines
    return '\n'.join(diamond) + '\n'

# Test cases using simple assertions
def test_diamond_A():
    expected_output = "A\n"
    assert print_diamond('A') == expected_output, "Test failed for input 'A'"

def test_diamond_B():
    expected_output = " A \nB B\n A \n"
    assert print_diamond('B') == expected_output, "Test failed for input 'B'"

def test_diamond_C():
    expected_output = "  A  \n B B \nC   C\n B B \n  A  \n"
    assert print_diamond('C') == expected_output, "Test failed for input 'C'"

# Run all the tests
def run_tests():
    test_diamond_A()
    test_diamond_B()
    test_diamond_C()
    print("All tests passed!")

# Run the tests to verify the function works correctly
run_tests()

# Interactive part: prompt the user for input and print the diamond
user_input = input("Insert character: ").upper()

# Validate the input and print the diamond if valid
if 'A' <= user_input <= 'Z':
    print(print_diamond(user_input))
else:
    print("Please enter a valid letter from A to Z.")