
def main():
    A = int(input())
    B = int(input())
    C = int(input())

    if A < B < C:
        if A + B < C:
            print(1)
        else:
            print(2)
    elif A == B == C:
        print(3)
    else:
        if A == B and B < C:
            if A + B < C:
                print(1)
            else:
                print(2)
        elif A < B and B == C:
            if A + B < C:
                print(1)
            else:
                print(2)
        else:
            print(2)

if __name__ == "__main__":
    main()
