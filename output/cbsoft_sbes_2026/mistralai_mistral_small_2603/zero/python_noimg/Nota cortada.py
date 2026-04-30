
def main():
    B = int(input())
    T = int(input())
    area_total = 160 * 70
    area_Felix = (B + T) * 70 / 2
    area_Marzia = area_total - area_Felix
    if area_Felix > area_Marzia:
        print(1)
    elif area_Marzia > area_Felix:
        print(2)
    else:
        print(0)

if __name__ == '__main__':
    main()
