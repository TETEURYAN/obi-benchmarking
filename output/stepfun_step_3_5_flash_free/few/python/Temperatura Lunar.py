import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    resultados = []
    while idx < len(data):
        n = int(data[idx]); m = int(data[idx+1]); idx += 2
        if n == 0 and m == 0:
            break
        temps = list(map(int, data[idx:idx+n]))
        idx += n
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + temps[i]
        min_media = None
        max_media = None
        for i in range(n - m + 1):
            soma = prefix[i+m] - prefix[i]
            media = int(soma / m)
            if min_media is None or media < min_media:
                min_media = media
            if max_media is None or media > max_media:
                max_media = media
        resultados.append((min_media, max_media))
    
    for i, (min_m, max_m) in enumerate(resultados):
        print(f"Teste {i+1}")
        print(f"{min_m} {max_m}")
        if i < len(resultados)-1:
            print()

if __name__ == "__main__":
    main()