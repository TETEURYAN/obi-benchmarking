
k = int(input())
l = int(input())

if (k <= 8 and l <= 8) or (k > 8 and l > 8):
    if (k <= 4 and l <= 4) or (k > 4 and l > 4):
        if (k <= 2 and l <= 2) or (k > 2 and l > 2):
            print("oitavas")
        else:
            print("quartas")
    else:
        print("semifinal")
else:
    print("final")
