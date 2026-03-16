import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    H = int(input_data[0])
    M = int(input_data[1])
    S = int(input_data[2])
    T = int(input_data[3])
    
    total_seconds = H * 3600 + M * 60 + S + T
    
    new_S = total_seconds % 60
    total_minutes = total_seconds // 60
    new_M = total_minutes % 60
    total_hours = total_minutes // 60
    new_H = total_hours % 24
    
    print(new_H)
    print(new_M)
    print(new_S)

if __name__ == '__main__':
    main()