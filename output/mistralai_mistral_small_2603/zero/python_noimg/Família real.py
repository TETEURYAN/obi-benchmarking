
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    idx = 0
    N, M = int(data[idx]), int(data[idx+1])
    idx += 2
    parents = list(map(int, data[idx:idx+N]))
    idx += N
    attendees = list(map(int, data[idx:idx+M]))

    parent_to_children = defaultdict(list)
    for child in range(1, N+1):
        parent = parents[child-1]
        parent_to_children[parent].append(child)

    generations = []
    queue = [0]
    while queue:
        current_gen = []
        next_queue = []
        for node in queue:
            current_gen.append(node)
            for child in parent_to_children[node]:
                next_queue.append(child)
        generations.append(current_gen)
        queue = next_queue

    present = set(attendees)
    percentages = []
    for gen in generations[1:]:
        total = len(gen)
        if total == 0:
            percentages.append(0.0)
            continue
        count = sum(1 for node in gen if node in present)
        percentage = (count / total) * 100
        percentages.append(round(percentage, 2))

    formatted = [f"{p:.2f}" for p in percentages]
    print(' '.join(formatted))

if __name__ == "__main__":
    main()
