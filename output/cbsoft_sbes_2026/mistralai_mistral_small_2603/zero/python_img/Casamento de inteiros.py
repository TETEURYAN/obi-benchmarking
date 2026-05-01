
def casamento(A, B):
    str_A = str(A)
    str_B = str(B)
    max_len = max(len(str_A), len(str_B))
    str_A = str_A.zfill(max_len)
    str_B = str_B.zfill(max_len)

    result_A = []
    result_B = []

    for a, b in zip(str_A, str_B):
        a_digit = int(a)
        b_digit = int(b)
        if a_digit < b_digit:
            result_B.append(b)
        elif b_digit < a_digit:
            result_A.append(a)
        # if equal, neither is added

    num_A = int(''.join(result_A)) if result_A else -1
    num_B = int(''.join(result_B)) if result_B else -1

    return num_A, num_B

def main():
    A = int(input().strip())
    B = int(input().strip())
    num_A, num_B = casamento(A, B)
    if num_A == -1 and num_B == -1:
        print("-1 -1")
    elif num_A == -1:
        print(f"-1 {num_B}")
    elif num_B == -1:
        print(f"{num_A} -1")
    else:
        if num_A <= num_B:
            print(f"{num_A} {num_B}")
        else:
            print(f"{num_B} {num_A}")

if __name__ == "__main__":
    main()
