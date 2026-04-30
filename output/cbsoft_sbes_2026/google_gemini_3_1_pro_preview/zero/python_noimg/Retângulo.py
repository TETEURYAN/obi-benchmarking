import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    L = [int(x) for x in input_data[1:N+1]]
    
    C = sum(L)
    if C % 2 != 0:
        print('N')
        return
        
    target = C // 2
    
    pos_set = set()
    positions = []
    current_pos = 0
    for length in L:
        positions.append(current_pos)
        pos_set.add(current_pos)
        current_pos += length
        
    pairs = 0
    for p in positions:
        if p < target:
            if (p + target) in pos_set:
                pairs += 1
                if pairs == 2:
                    print('S')
                    return
        else:
            break
            
    print('N')

if __name__ == '__main__':
    main()