
n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

half = n // 2

# Corte horizontal: uma figurinha nas linhas 1..half e outra em half+1..n
if (x1 <= half and x2 > half) or (x2 <= half and x1 > half):
    print("S")
# Corte vertical: uma figurinha nas colunas 1..half e outra em half+1..n
elif (y1 <= half and y2 > half) or (y2 <= half and y1 > half):
    print("S")
else:
    print("N")
