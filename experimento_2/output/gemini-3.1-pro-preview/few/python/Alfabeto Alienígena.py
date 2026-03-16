import sys

input_data = sys.stdin.read().split()
if len(input_data) >= 4:
    alphabet = set(input_data[2])
    message = input_data[3]
    
    for char in message:
        if char not in alphabet:
            print('N')
            break
    else:
        print('S')