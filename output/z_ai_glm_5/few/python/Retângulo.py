import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n_str = next(iterator)
        n = int(n_str)
    except StopIteration:
        return

    if n < 4:
        print("N")
        return

    lengths = []
    for _ in range(n):
        try:
            lengths.append(int(next(iterator)))
        except StopIteration:
            break
    
    if len(lengths) != n:
        return

    total_circumference = sum(lengths)

    if total_circumference % 2 != 0:
        print("N")
        return

    target_dist = total_circumference // 2

    positions = set()
    current_pos = 0
    positions.add(current_pos)
    
    for i in range(n - 1):
        current_pos += lengths[i]
        positions.add(current_pos)

    pairs_count = 0
    for p in positions:
        if (p + target_dist) in positions:
            pairs_count += 1

    if pairs_count >= 4:
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    solve()