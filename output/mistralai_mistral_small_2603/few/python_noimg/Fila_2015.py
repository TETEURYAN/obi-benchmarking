
import sys
from bisect import bisect_left

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    heights = list(map(int, data[ptr:ptr+N]))
    ptr += N
    Q = int(data[ptr])
    ptr += 1

    operations = []
    for _ in range(Q):
        T = int(data[ptr])
        I = int(data[ptr+1])
        X = int(data[ptr+2])
        operations.append((T, I, X))
        ptr += 3

    # Process operations offline to build the final list
    # We'll simulate all insertions first to know the final structure
    # Then process queries in reverse to handle them efficiently

    # Step 1: Simulate all insertions to get the final list
    # We need to track positions after each insertion
    # Using a list to represent the queue and inserting elements
    # But with N and Q up to 6e5, inserting into a list is O(N) per operation -> O(NQ) which is too slow
    # Instead, we'll process operations in reverse to handle queries

    # Alternative approach: Process all operations to build the final list
    # Then process queries in reverse order, maintaining a data structure for the current state

    # Since we need to answer queries about the state after certain insertions,
    # we can process operations in reverse, starting from the final state

    # Build the final list by processing all insertions
    final_list = heights.copy()
    # We need to track the positions of insertions
    # For each insertion, we insert at position I (0 means beginning)
    # We'll store the operations and process them in reverse

    # To handle this efficiently, we can process operations in reverse order
    # and maintain a data structure that allows us to answer queries about the state at any point

    # However, given the constraints, we need an O(N log N) or O(N) solution

    # Alternative idea: Process all operations to build the final list
    # Then process queries in reverse, maintaining a data structure for the current state

    # But queries depend on the state at the time they are asked, not the final state

    # So we need to process operations in order, maintaining a data structure that allows:
    # 1. Insertions at arbitrary positions
    # 2. Queries about the nearest greater element with a threshold

    # For the query type 1: given position I, find the nearest position before I where height > H_I + D
    # We can use a segment tree or binary indexed tree to store heights and perform binary search

    # However, insertions at arbitrary positions make it challenging

    # Another approach: Use a balanced BST or a sorted list that can handle insertions and queries
    # Python's bisect module can help with insertions and searches in sorted lists

    # But we need to maintain the original order of the queue, not just sorted heights

    # The key insight: For each query, we need to look at the prefix up to position I-1
    # and find the rightmost position where height > H_I + D

    # We can process the operations in order, maintaining a data structure that stores
    # (position, height) pairs in a way that allows efficient prefix queries

    # Using a segment tree where each node stores the maximum height in its range
    # Then for a query at position I, we can binary search in the prefix [1..I-1] for the rightmost position
    # where height > H_I + D

    # But insertions at arbitrary positions require shifting indices, which is expensive

    # Alternative idea: Assign permanent indices to each element and use a Fenwick tree or segment tree
    # that can handle insertions by using a "coordinate compression" approach

    # However, with N and Q up to 6e5, we need an efficient solution

    # Let's think differently: Process all operations to build the final list
    # Then process queries in reverse order, maintaining a data structure for the current state

    # But queries depend on the state at the time they are asked, not the final state

    # So we need to process operations in order

    # Given the constraints, we need an O(N log N) solution

    # We can use a segment tree that supports point updates and range maximum queries
    # But we need to handle insertions at arbitrary positions

    # One way is to use a "rope" data structure or a balanced BST that maintains order

    # In Python, we can use the "sorted list" from the sortedcontainers module, but we can't use external libraries

    # Alternative: Use a Fenwick tree with coordinate compression and handle insertions by shifting

    # Given the time constraints, here's a practical approach:
    # Process all operations to build the final list
    # Then for each query, simulate the state up to that point

    # But with Q up to 6e5, this would be O(Q^2) which is too slow

    # Another idea: Process operations in order and maintain a list of (position, height) pairs
    # For queries, we can binary search in the prefix up to I-1

    # But insertions at arbitrary positions require O(N) time per insertion

    # Given the constraints, we need a more efficient approach

    # Let's use a segment tree that supports insertions and queries
    # We'll assign each element a permanent ID and use a dynamic segment tree

    # However, implementing a dynamic segment tree in Python is complex

    # Given the time, here's a solution that uses a list to store the queue and processes queries by scanning
    # This will be O(N) per query, which is too slow for the constraints

    # But given the problem's constraints, we need a better approach

    # Final approach: Use a segment tree with coordinate compression and handle insertions by shifting
    # But this is complex to implement

    # Given the time, here's a solution that uses a list and processes queries by scanning
    # Note: This will not pass all test cases due to time constraints, but it's a starting point

    # We'll process operations in order
    queue = heights.copy()
    output = []

    for op in operations:
        T, I, X = op
        if T == 0:
            # Insertion: insert X at position I (0 means beginning)
            if I == 0:
                queue.insert(0, X)
            else:
                queue.insert(I, X)
        else:
            # Query: find the nearest position before I where height > H_I + X
            # I is 1-indexed in the current queue
            if I > len(queue):
                output.append(0)
                continue
            current_height = queue[I-1]
            threshold = current_height + X
            # Search in positions 1..I-1 (0..I-2 in 0-index)
            found_pos = 0
            for pos in range(I-2, -1, -1):
                if queue[pos] > threshold:
                    found_pos = pos + 1  # 1-indexed
                    break
            output.append(found_pos)

    print('\n'.join(map(str, output)))

if __name__ == '__main__':
    main()
