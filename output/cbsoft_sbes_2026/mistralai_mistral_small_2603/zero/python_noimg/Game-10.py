
def main():
    N = int(input())
    D = int(input())
    A = int(input())

    if D == A:
        print(0)
    else:
        clockwise = (D - A) % N
        counter_clockwise = (A - D) % N
        print(min(clockwise, counter_clockwise))

if __name__ == "__main__":
    main()
