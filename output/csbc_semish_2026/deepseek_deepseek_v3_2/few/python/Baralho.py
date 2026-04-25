import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return

    suits = {'C': [0]*14, 'E': [0]*14, 'U': [0]*14, 'P': [0]*14}
    n = len(data)
    i = 0
    while i < n:
        card = data[i:i+3]
        i += 3
        value = int(card[0:2])
        suit = card[2]
        suits[suit][value] += 1

    for suit in ['C', 'E', 'U', 'P']:
        arr = suits[suit]
        error = False
        missing = 0
        for v in range(1, 14):
            if arr[v] > 1:
                error = True
                break
            elif arr[v] == 0:
                missing += 1
        if error:
            print("erro")
        else:
            print(missing)

if __name__ == "__main__":
    main()