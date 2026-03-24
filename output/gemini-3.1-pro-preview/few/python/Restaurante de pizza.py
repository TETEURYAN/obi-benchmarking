import sys

input_data = sys.stdin.read().split()
if input_data:
    A = int(input_data[0])
    B = int(input_data[1])
    R = int(input_data[2])
    G = int(input_data[3])
    
    if 2 * R <= A and 2 * R <= B and 360 % G == 0:
        print('S')
    else:
        print('N')