import sys

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    count_invisible = 0
    max_from_right = 0
    
    for i in range(n-1, -1, -1):
        if i == n-1:
            max_from_right = a[i]
        else:
            if max_from_right >= a[i]:
                count_invisible += 1
            else:
                max_from_right = a[i]
    
    print(count_invisible)

main()