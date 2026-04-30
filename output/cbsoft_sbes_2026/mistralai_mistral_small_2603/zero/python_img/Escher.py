
def main():
    n = int(input().strip())
    heights = list(map(int, input().split()))

    is_escher = True
    for i in range(n // 2):
        if heights[i] + heights[n - 1 - i] != heights[i + 1] + heights[n - 2 - i]:
            is_escher = False
            break

    print('S' if is_escher else 'N')

if __name__ == "__main__":
    main()
