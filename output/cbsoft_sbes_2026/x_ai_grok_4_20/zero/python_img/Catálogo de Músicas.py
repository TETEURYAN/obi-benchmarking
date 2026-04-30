
import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.files_here = 0
        self.subtree_files = 0
        self.subtree_nodes = 0
        self.name_len = 0

def build_trie(paths):
    root = TrieNode()
    for path in paths:
        parts = path.split('/')
        node = root
        for i, part in enumerate(parts):
            if part not in node.children:
                node.children[part] = TrieNode()
                if i < len(parts) - 1 or not part.endswith('.'):
                    node.children[part].name_len = len(part)
            node = node.children[part]
        node.is_file = True
    return root

def dfs(node, depth):
    node.subtree_files = node.files_here
    node.subtree_nodes = 1
    total = 0
    for child in node.children.values():
        if child.is_file:
            child.files_here = 1
            child.subtree_files = 1
            child.subtree_nodes = 1
            total += child.name_len
        else:
            total += dfs(child, depth + 1)
            node.subtree_files += child.subtree_files
            node.subtree_nodes += child.subtree_nodes
    if node.is_file:
        node.files_here = 1
        node.subtree_files += 1
    return total

def compute_cost(node, ref_depth, current_depth, ref_node):
    if node.subtree_files == 0:
        return 0
    if ref_node is None:
        base = sum(len(name) + 1 for name in node.children if not node.children[name].is_file) + sum(c.name_len for c in node.children.values() if c.is_file)
        for child_name, child in node.children.items():
            if not child.is_file:
                base += compute_cost(child, 0, current_depth + 1, None)
        return base
    savings = 0
    best = float('inf')
    for d in range(current_depth + 1):
        cost = 0
        up = current_depth - d
        if up > 0:
            cost += up * 3
        if d > 0:
            cost += ref_node.name_len + 1
        cost += node.name_len if d > 0 else 0
        if cost > 0 and node.subtree_files > 0:
            cost += (node.subtree_files - 1)
        best = min(best, cost)
    total = best
    for child_name, child in node.children.items():
        if not child.is_file:
            total += compute_cost(child, ref_depth, current_depth + 1, node if ref_node is None else ref_node)
    return total

def main():
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    paths = data[1:1+N]
    if N == 0:
        print(0)
        return
    root = build_trie(paths)
    dfs(root, 0)
    min_chars = float('inf')
    def try_ref(node, depth):
        nonlocal min_chars
        if node.subtree_files == 0:
            return
        cost = compute_cost(root, 0, 0, node if depth > 0 else None)
        min_chars = min(min_chars, cost)
        for child_name, child in node.children.items():
            if not child.is_file:
                try_ref(child, depth + 1)
    try_ref(root, 0)
    print(min_chars)

if __name__ == "__main__":
    main()
