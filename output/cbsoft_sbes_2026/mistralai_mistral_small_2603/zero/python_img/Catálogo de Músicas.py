
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    N = int(data[0])
    paths = data[1:N+1]

    tree = defaultdict(list)
    root = {}
    all_nodes = set()

    for path in paths:
        parts = path.split('/')
        current = root
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
            all_nodes.add(part)
        file_name = parts[-1]
        current[file_name] = None
        all_nodes.add(file_name)

    all_nodes = list(all_nodes)
    min_total = float('inf')

    for ref in all_nodes:
        total = 0
        for path in paths:
            parts = path.split('/')
            ref_index = -1
            for i, part in enumerate(parts):
                if part == ref:
                    ref_index = i
                    break
            if ref_index == -1:
                total += len(path) + 3 * (len(parts) - 1)
            else:
                new_path_parts = []
                for i in range(ref_index + 1, len(parts)):
                    new_path_parts.append(parts[i])
                if ref_index > 0:
                    new_path_parts = ['..'] * ref_index + new_path_parts
                new_path = '/'.join(new_path_parts)
                total += len(new_path)
        if total < min_total:
            min_total = total
    print(min_total)

if __name__ == "__main__":
    main()
