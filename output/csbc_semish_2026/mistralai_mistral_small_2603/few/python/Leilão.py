import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    index = 1
    max_value = -1
    winner_name = ""

    for _ in range(n):
        name = data[index]
        value = int(data[index + 1])
        index += 2
        if value > max_value:
            max_value = value
            winner_name = name

    print(winner_name)
    print(max_value)

if __name__ == "__main__":
    main()