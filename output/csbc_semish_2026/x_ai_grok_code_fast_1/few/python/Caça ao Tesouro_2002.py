import sys

data = sys.stdin.read().split()
idx = 0
teste = 1

while True:
    X = int(data[idx])
    Y = int(data[idx + 1])
    N = int(data[idx + 2])
    idx += 3
    if X == 0 and Y == 0 and N == 0:
        break
    
    valores = []
    for _ in range(N):
        valores.append(int(data[idx]))
        idx += 1
    
    total_arca = sum(valores)
    target = Y + total_arca - X
    if target % 2 != 0 or target < 0:
        print(f"Teste {teste}")
        print("N")
        print()
        teste += 1
        continue
    
    target //= 2
    if target > total_arca or target < 0:
        print(f"Teste {teste}")
        print("N")
        print()
        teste += 1
        continue
    
    # DP para subset sum
    dp = [False] * (target + 1)
    dp[0] = True
    for v in valores:
        for j in range(target, v - 1, -1):
            if dp[j - v]:
                dp[j] = True
    
    print(f"Teste {teste}")
    if dp[target]:
        print("S")
    else:
        print("N")
    print()
    teste += 1