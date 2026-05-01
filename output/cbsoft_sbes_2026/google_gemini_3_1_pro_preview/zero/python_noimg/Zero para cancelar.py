import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    stack = []
    
    for i in range(1, n + 1):
        x = int(input_data[i])
        if x == 0:
            if stack:
                stack.pop()
        else:
            stack.append(x)
            
    print(sum(stack))

if __name__ == '__main__':
    main()