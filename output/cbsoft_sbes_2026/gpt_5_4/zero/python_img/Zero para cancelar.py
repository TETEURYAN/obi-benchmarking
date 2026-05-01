import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    stack = []
    
    for i in range(1, n + 1):
        x = int(data[i])
        if x == 0:
            stack.pop()
        else:
            stack.append(x)
    
    print(sum(stack))

if __name__ == "__main__":
    main()