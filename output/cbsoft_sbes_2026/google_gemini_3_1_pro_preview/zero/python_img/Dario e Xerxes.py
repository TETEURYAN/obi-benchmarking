import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    dario = 0
    xerxes = 0
    
    for i in range(1, 2 * n + 1, 2):
        d = int(input_data[i])
        x = int(input_data[i+1])
        
        if (x - d) % 5 in (1, 2):
            dario += 1
        else:
            xerxes += 1
            
    if dario > xerxes:
        print("dario")
    else:
        print("xerxes")

if __name__ == '__main__':
    main()