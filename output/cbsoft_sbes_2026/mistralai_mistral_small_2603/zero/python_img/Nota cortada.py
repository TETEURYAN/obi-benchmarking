
def main():
    B = int(input())
    T = int(input())
    area_total = 160 * 70
    area_felix = 0.5 * (B + T) * 70
    area_marzia = area_total - area_felix
    if area_felix > area_marzia:
        print(1)
    elif area_marzia > area_felix:
        print(2)
    else:
        print(0)

if __name__ == "__main__":
    main()
