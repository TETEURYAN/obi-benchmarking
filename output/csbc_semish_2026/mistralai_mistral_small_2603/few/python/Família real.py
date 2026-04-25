
import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2

    parents = list(map(int, data[idx:idx + N]))
    idx += N

    attendees = list(map(int, data[idx:idx + M]))

    # Build the tree structure
    children = defaultdict(list)
    for i in range(1, N + 1):
        parent = parents[i - 1]
        children[parent].append(i)

    # Determine generations
    generations = defaultdict(list)
    queue = deque()
    queue.append((0, 0))  # (node, generation)

    while queue:
        node, gen = queue.popleft()
        generations[gen].append(node)
        for child in children[node]:
            queue.append((child, gen + 1))

    # Count attendees per generation
    gen_attendees = defaultdict(int)
    for attendee in attendees:
        for gen, nodes in generations.items():
            if attendee in nodes:
                gen_attendees[gen] += 1
                break

    # Calculate percentages
    output = []
    for gen in sorted(generations.keys()):
        total = len(generations[gen])
        if total == 0:
            output.append("0.00")
            continue
        percentage = (gen_attendees[gen] / total) * 100
        output.append(f"{percentage:.2f}")

    print(' '.join(output))

if __name__ == "__main__":
    main()
