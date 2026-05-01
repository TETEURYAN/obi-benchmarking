import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    n = int(input_data[0])
    instructions = input_data[1]
    
    room = 1
    for char in instructions:
        if char == 'E':
            room = room * 2
        elif char == 'D':
            room = room * 2 + 1
            
    print(room)

if __name__ == '__main__':
    main()