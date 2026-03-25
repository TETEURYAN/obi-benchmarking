import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    sizes = list(map(int, data[1:1+n]))
    
    substituidos = 0
    consertados = 0
    
    for size in sizes:
        if size < 50:
            substituidos += 1
        elif size < 85:
            consertados += 1
    
    print(substituidos, consertados)

if __name__ == "__main__":
    main()