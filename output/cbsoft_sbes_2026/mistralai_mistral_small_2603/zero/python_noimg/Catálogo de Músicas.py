
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    paths = data[1:n+1]

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
        all_nodes.add(parts[-1])

    nodes = list(all_nodes)
    min_total = float('inf')

    for ref in nodes:
        total = 0
        for path in paths:
            parts = path.split('/')
            if ref in parts:
                idx = parts.index(ref)
                new_path = parts[idx:]
                new_path_str = '/'.join(new_path)
                if idx > 0:
                    new_path_str = '../' * idx + new_path_str
                total += len(new_path_str)
            else:
                total += len(path)
        if total < min_total:
            min_total = total

    print(min_total)

if __name__ == '__main__':
    main()
