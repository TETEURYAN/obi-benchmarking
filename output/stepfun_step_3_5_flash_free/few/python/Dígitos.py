import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    digitos = list(map(int, data[1:1+n]))
    S = ''.join(str(d) for d in digitos)
    if S[0] == '0':
        print(-1)
        return
    for L in range(1, n+1):
        x = int(S[:L])
        i = L
        atual = x
        while i < n:
            prox = atual + 1
            s_prox = str(prox)
            if i + len(s_prox) > n or S[i:i+len(s_prox)] != s_prox:
                break
            i += len(s_prox)
            atual = prox
        else:
            print(x)
            return
    print(-1)

if __name__ == "__main__":
    main()