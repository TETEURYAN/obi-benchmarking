
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    notas = list(map(int, data[1:n+1]))
    
    freq = defaultdict(int)
    for nota in notas:
        freq[nota] += 1
    
    max_freq = max(freq.values())
    candidatos = [nota for nota, count in freq.items() if count == max_freq]
    print(max(candidatos))

if __name__ == "__main__":
    main()
