import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    a_str = data[0]
    b_str = data[1]

    max_len = max(len(a_str), len(b_str))
    a_pad = a_str.zfill(max_len)
    b_pad = b_str.zfill(max_len)

    a_res = []
    b_res = []

    for i in range(max_len):
        da = a_pad[i]
        db = b_pad[i]
        if da < db:
            a_res.append(da)
        elif db < da:
            b_res.append(db)
        else:
            a_res.append(da)
            b_res.append(db)

    a_ans = ''.join(a_res).lstrip('0') if a_res else ''
    b_ans = ''.join(b_res).lstrip('0') if b_res else ''

    if not a_ans:
        a_ans = '-1'
    elif a_ans == '':
        a_ans = '0'
    if not b_ans:
        b_ans = '-1'
    elif b_ans == '':
        b_ans = '0'

    nums = [int(a_ans), int(b_ans)]
    nums.sort()
    print(nums[0], nums[1])

if __name__ == "__main__":
    solve()