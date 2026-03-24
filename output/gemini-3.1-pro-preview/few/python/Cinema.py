import sys

def get_price(age):
    if age <= 17:
        return 15
    elif age <= 59:
        return 30
    else:
        return 20

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        age1 = int(input_data[0])
        age2 = int(input_data[1])
        print(get_price(age1) + get_price(age2))

if __name__ == '__main__':
    main()