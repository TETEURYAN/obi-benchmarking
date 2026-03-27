
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    C = int(data[0])
    queries = list(map(int, data[1:C+1]))
    stock = set()
    manufactured = 0
    for length in queries:
        if length in stock:
            stock.remove(length)
        else:
            manufactured += 2
            stock.add(length)
    print(manufactured)

if __name__ == "__main__":
    main()
