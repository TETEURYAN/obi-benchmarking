import sys

def build_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            pi[i] = length
            i += 1
        else:
            if length != 0:
                length = pi[length - 1]
            else:
                pi[i] = 0
                i += 1
    return pi

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return True
    pi = build_prefix_function(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return True
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1
    return False

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    strings = data[1:1+n]
    
    if n <= 2:
        print("ok")
        return
    
    for k in range(2, n):
        sk = strings[k]
        found = False
        for a in range(k):
            for b in range(k):
                concat = strings[a] + strings[b]
                if kmp_search(concat, sk):
                    print(sk)
                    return
    print("ok")

if __name__ == "__main__":
    main()