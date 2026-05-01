import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = input_data[0]
    M = int(input_data[1])
    words = input_data[2:]
    
    trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', '22233344455566677778889999')
    
    count = 0
    for word in words:
        if len(word) == len(N):
            if word.translate(trans) == N:
                count += 1
                
    print(count)

if __name__ == '__main__':
    main()