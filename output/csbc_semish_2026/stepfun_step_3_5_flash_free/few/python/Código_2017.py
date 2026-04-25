import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    strings = data[1:1+n]
    
    set_strings = set()
    set_prefixes = set()
    set_suffixes = set()
    
    for s in strings:
        if s in set_strings:
            print(s)
            return
        
        for i in range(1, 10):
            x = s[:i]
            y = s[i:]
            if x in set_suffixes and y in set_prefixes:
                print(s)
                return
        
        set_strings.add(s)
        for i in range(1, 10):
            set_prefixes.add(s[:i])
            set_suffixes.add(s[10-i:])
    
    print("ok")

if __name__ == "__main__":
    main()