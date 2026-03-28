import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    notas = list(map(int, data[1:1+n]))
    
    freq = [0] * 101
    for nota in notas:
        freq[nota] += 1
        
    best_note = 0
    best_freq = 0
    for nota in range(100, -1, -1):
        if freq[nota] > best_freq:
            best_freq = freq[nota]
            best_note = nota
            
    print(best_note)

if __name__ == "__main__":
    main()