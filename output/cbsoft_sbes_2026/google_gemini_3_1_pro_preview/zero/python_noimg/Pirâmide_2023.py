import sys

def main():
    input_str = sys.stdin.read().split()
    if not input_str:
        return
    w = [int(x) for x in input_str]
    s = sum(w)
    
    if s % 3 != 0:
        print("N")
        return
        
    t = s // 3
    
    if t not in w:
        print("N")
        return
        
    w.remove(t)
    
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            if w[i] + w[j] == t:
                print("S")
                return
                
    print("N")

if __name__ == '__main__':
    main()