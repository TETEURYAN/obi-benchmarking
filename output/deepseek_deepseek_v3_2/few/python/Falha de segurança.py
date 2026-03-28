import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    passwords = data[1:1+n]
    
    # Build trie
    trie = [{}]
    end = [[] for _ in range(200000)]  # list of indices where this node is end of some password
    node_count = 1
    
    for idx, s in enumerate(passwords):
        node = 0
        for ch in s:
            if ch not in trie[node]:
                trie[node][ch] = node_count
                trie.append({})
                end.append([])
                node_count += 1
            node = trie[node][ch]
        end[node].append(idx)
    
    # For each password, find all passwords that contain it as substring
    total = 0
    for i, s in enumerate(passwords):
        node = 0
        for ch in s:
            if ch not in trie[node]:
                break
            node = trie[node][ch]
            # All passwords that end at or below this node are contained
            stack = [node]
            while stack:
                cur = stack.pop()
                total += len(end[cur])
                for nxt in trie[cur].values():
                    stack.append(nxt)
        # Remove self-match
        total -= 1
    
    print(total)

if __name__ == "__main__":
    main()