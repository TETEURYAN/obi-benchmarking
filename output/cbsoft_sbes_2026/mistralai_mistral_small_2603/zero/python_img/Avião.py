
def main():
    F, C, E, B = map(int, input().split())
    total_economica = F - E + 1
    assentos_economica = total_economica * C
    if B > assentos_economica:
        print("PROXIMO VOO")
    else:
        fileira = E + (B - 1) // C
        posicao = chr(ord('A') + (B - 1) % C)
        print(f"{fileira} {posicao}")

if __name__ == "__main__":
    main()
