
def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    if A == B + C + D and B + C == D and B == C:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
