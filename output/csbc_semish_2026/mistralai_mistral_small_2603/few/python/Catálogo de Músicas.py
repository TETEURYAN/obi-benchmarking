
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    paths = data[1:n+1]

    tree = defaultdict(list)
    root = 'root'
    folder_depth = {root: 0}
    folder_parent = {root: None}

    for path in paths:
        parts = path.split('/')
        current = root
        for part in parts[:-1]:
            if part not in tree[current]:
                tree[current].append(part)
                folder_parent[part] = current
                folder_depth[part] = folder_depth[current] + 1
            current = part

    def get_path_length(path, reference):
        parts = path.split('/')
        ref_parts = reference.split('/') if reference != root else []
        common_prefix_len = 0
        min_len = min(len(parts) - 1, len(ref_parts))
        while common_prefix_len < min_len and parts[common_prefix_len] == ref_parts[common_prefix_len]:
            common_prefix_len += 1

        up_steps = len(ref_parts) - common_prefix_len
        down_steps = (len(parts) - 1) - common_prefix_len
        total_length = up_steps * 3 + down_steps
        for i in range(common_prefix_len, len(parts)):
            total_length += len(parts[i])
            if i < len(parts) - 1:
                total_length += 1
        return total_length

    min_total = float('inf')
    for reference in folder_parent:
        total = 0
        for path in paths:
            total += get_path_length(path, reference)
        if total < min_total:
            min_total = total
    print(min_total)

if __name__ == '__main__':
    main()
