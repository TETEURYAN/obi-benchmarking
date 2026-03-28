import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    C = int(data[0])
    queries = list(map(int, data[1:1+C]))
    
    estoque = set()
    fabricados = 0
    
    for comp in queries:
        if comp in estoque:
            estoque.remove(comp)
        else:
            fabricados += 2
            estoque.add(comp)
    
    print(fabricados)

if __name__ == "__main__":
    main()