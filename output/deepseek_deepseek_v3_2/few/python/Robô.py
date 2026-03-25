import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    C = int(data[1])
    S = int(data[2])
    commands = list(map(int, data[3:3+C]))
    
    pos = 1  # início na estação 1
    count = 0
    
    # verifica a posição inicial antes de qualquer comando
    if pos == S:
        count += 1
    
    for x in commands:
        if x == 1:
            pos = (pos + 1) % N
        else:
            pos = (pos - 1) % N
        if pos == 0:
            pos = N
        if pos == S:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()