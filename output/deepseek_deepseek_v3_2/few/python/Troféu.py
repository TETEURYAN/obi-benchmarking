import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    scores = list(map(int, data[:5]))
    
    max_score = scores[0]
    trophies = 1
    for i in range(1, 5):
        if scores[i] == max_score:
            trophies += 1
        else:
            break
    
    if trophies == 5:
        print(f"{trophies} 0")
        return
    
    second_score = scores[trophies]
    plaques = 1
    for i in range(trophies + 1, 5):
        if scores[i] == second_score:
            plaques += 1
        else:
            break
    
    print(f"{trophies} {plaques}")

if __name__ == "__main__":
    main()