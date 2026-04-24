import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N = int(data[0])
    queue_ids = list(map(int, data[1:1+N]))
    M = int(data[1+N])
    left_ids = set(map(int, data[1+N+1:1+N+1+M]))

    # Mantém apenas os IDs que não saíram
    result = [id for id in queue_ids if id not in left_ids]

    # Imprime o resultado separado por espaço
    print(*result)

if __name__ == "__main__":
    main()