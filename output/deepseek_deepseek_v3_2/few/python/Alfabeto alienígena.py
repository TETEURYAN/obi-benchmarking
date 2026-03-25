import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    K = int(data[0])
    N = int(data[1])
    alphabet = data[2]
    message = data[3]
    
    allowed = set(alphabet)
    
    for ch in message:
        if ch not in allowed:
            print('N')
            return
    
    print('S')

if __name__ == "__main__":
    main()