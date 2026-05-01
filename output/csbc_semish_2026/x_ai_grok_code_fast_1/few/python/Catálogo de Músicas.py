import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.files = []
        self.C = 0
        self.S = 0
        self.D = 0
        self.LenR = 0

def build_tree(paths):
    root = Node('')
    for path in paths:
        parts = path.split('/')
        current = root
        for p in parts[:-1]:
            if p not in current.children:
                current.children[p] = Node(p)
            current = current.children[p]
        current.files.append(parts[-1])
    return root

def dfs(node, depth, len_so_far):
    node.D = depth
    node.LenR = len_so_far
    C = 0
    S = 0
    for child_name, child in node.children.items():
        child_len = len_so_far + len(child_name) + 1
        c, s = dfs(child, depth + 1, child_len)
        C += c
        S += s
    for file in node.files:
        Lf = len_so_far + 1 + len(file)
        C += 1
        S += Lf
    node.C = C
    node.S = S
    return C, S

def collect_nodes(node, nodes):
    nodes.append(node)
    for child in node.children.values():
        collect_nodes(child, nodes)

input_data = sys.stdin.read().splitlines()
N = int(input_data[0])
paths = input_data[1:]

root = build_tree(paths)
dfs(root, 0, 0)
N_total = root.C
sum_all_Lf = root.S

nodes = []
collect_nodes(root, nodes)

min_cost = float('inf')
for node in nodes:
    cost = node.S - node.C * node.LenR + 3 * node.D * (N_total - node.C) + sum_all_Lf
    if cost < min_cost:
        min_cost = cost

print(min_cost)