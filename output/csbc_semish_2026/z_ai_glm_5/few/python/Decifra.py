import sys

# Define a recursion limit higher than default, as per guidelines for competitive programming
sys.setrecursionlimit(200000)

def main():
    # Read all input from stdin at once for performance

    input_data = sys.stdin.read().split()

    # Ensure there is enough data to process
    if len(input_data) < 2:
        return

    # The first token is the permutation string
    permutation = input_data[0]
    
    # The second token is the encrypted phrase
    # The problem states the phrase contains only lowercase letters, 
    # so split() correctly captures it as a single token.
    encrypted_phrase = input_data[1]

    # The problem states the permutation is "invertible" (a swap).
    # This means if 'a' maps to 'x', then 'x' maps to 'a'.
    # Therefore, applying the permutation mapping to the encrypted text 
    # will return the original text.
    
    # We create a translation table where the i-th letter of the alphabet
    # maps to the i-th letter of the permutation string.
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Check for valid permutation length (though constraints guarantee it)
    if len(permutation) != 26:
        return

    # Create the translation table
    # maketrans is efficient for character mapping
    translation_table = str.maketrans(original_alphabet, permutation)
    
    # Apply the translation to the encrypted phrase
    decrypted_phrase = encrypted_phrase.translate(translation_table)
    
    # Print the result to stdout
    print(decrypted_phrase)

if __name__ == '__main__':
    main()