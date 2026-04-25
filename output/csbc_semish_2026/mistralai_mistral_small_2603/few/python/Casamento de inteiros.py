
import sys

def casamento_inteiros(a, b):
    str_a = str(a)
    str_b = str(b)

    max_len = max(len(str_a), len(str_b))
    str_a = str_a.zfill(max_len)
    str_b = str_b.zfill(max_len)

    result_a = []
    result_b = []

    for da, db in zip(str_a, str_b):
        da_int = int(da)
        db_int = int(db)
        if da_int < db_int:
            result_b.append(db)
        elif db_int < da_int:
            result_a.append(da)
        else:
            result_a.append(da)
            result_b.append(db)

    num_a = int(''.join(result_a)) if result_a else -1
    num_b = int(''.join(result_b)) if result_b else -1

    if num_a > num_b:
        num_a, num_b = num_b, num_a

    return num_a, num_b

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    res_a, res_b = casamento_inteiros(a, b)
    print(f"{res_a} {res_b}")

if __name__ == "__main__":
    main()
