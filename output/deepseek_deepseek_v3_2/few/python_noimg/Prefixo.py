import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    word1 = data[idx]; idx += 1
    m = int(data[idx]); idx += 1
    word2 = data[idx]; idx += 1
    
    limit = min(n, m)
    ans = 0
    for i in range(limit):
        if word1[i] == word2[i]:
            ans += 1
        else:
            break
    
    print(ans)

if __name__ == "__main__":
    main()