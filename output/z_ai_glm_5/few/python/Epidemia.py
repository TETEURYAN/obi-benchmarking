import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    R = int(input_data[1])
    P = int(input_data[2])

    total_infected = N
    newly_infected = N
    days = 0

    while total_infected < P:
        newly_infected *= R
        total_infected += newly_infected
        days += 1

    print(days)

if __name__ == "__main__":
    main()