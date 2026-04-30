import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    posA = []
    for i in range(N):
        if input_data[2 + i] == '1':
            posA.append(i)
            
    posB = []
    for i in range(N):
        if input_data[2 + N + i] == '1':
            posB.append(i)
            
    ans = sum(abs(a - b) for a, b in zip(posA, posB))
    print(ans)

if __name__ == '__main__':
    main()