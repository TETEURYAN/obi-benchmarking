import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    c = int(data[0])
    lengths = list(map(int, data[1:1+c]))
    
    stock = set()
    manufactured = 0
    
    for l in lengths:
        if l in stock:
            stock.remove(l)
        else:
            stock.add(l)
            manufactured += 2
    
    print(manufactured)

if __name__ == "__main__":
    main()