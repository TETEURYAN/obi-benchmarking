import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    ans = [0] * (n + 1)
    
    for i in range(1, n + 1):
        ans[int(input_data[i])] = i
        
    sys.stdout.write('\n'.join(map(str, ans[1:])) + '\n')

if __name__ == '__main__':
    main()