import sys
from sys import stdin

def solve():
    input_data = stdin.read().split('\n')
    idx = 0
    N = int(input_data[idx]); idx += 1
    
    files = []
    for i in range(N):
        if idx < len(input_data):
            line = input_data[idx].strip(); idx += 1
            if line:
                files.append(line)
    
    # Parse each file path into components
    # Each file: list of parts (folders + filename)
    parsed = []
    for f in files:
        parts = f.split('/')
        parsed.append(parts)
    
    # Build a trie of all folder paths
    # We need to find the optimal reference folder (node in the trie)
    # that minimizes total catalog size
    
    # For each file, its path from root is: parts[0], parts[1], ..., parts[-2] (folders), parts[-1] (filename)
    # The folder path is parts[:-1], the file is parts[-1]
    
    # For a reference folder R at depth d with path r[0..d-1]:
    # For a file with folder path f[0..k-1]:
    #   - Find LCA of R and f[0..k-1]
    #   - Let LCA be at depth l (common prefix length)
    #   - Going up from R to LCA: (d - l) steps of '../'
    #   - Going down from LCA to file folder: f[l], f[l+1], ..., f[k-1]
    #   - Then filename
    # Cost = (d - l) * 3 + sum(len(f[j])+1 for j in l..k-1) + len(filename)
    # But if d == l and l == k (file is directly in R or subdir), cost is just relative path
    
    # Actually let me reconsider:
    # If reference is R with path r[0..d-1] (depth d):
    # For file with folder path f[0..k-1] and filename fn:
    #   common prefix length l = len of common prefix between r and f
    #   up_steps = d - l  (number of '../')
    #   down_parts = f[l:k]
    #   cost = up_steps * 3 + sum(len(p)+1 for p in down_parts) + len(fn)
    #   But if down_parts is empty and up_steps == 0: cost = len(fn)
    #   Otherwise if down_parts non-empty: last separator already counted
    #   Wait: path is like ../../Rock/Angra/file.mp3
    #   = up_steps * 3 chars + sum(len(p)+1 for p in down_parts) + len(fn)
    #   If up_steps==0 and down_parts empty: just len(fn)
    
    # Collect all unique folder paths as potential references
    # Also include root (empty path, depth 0)
    
    folder_set = set()
    folder_set.add(tuple())  # root
    for parts in parsed:
        folder_path = parts[:-1]
        for i in range(len(folder_path)+1):
            folder_set.add(tuple(folder_path[:i]))
    
    # Precompute for each file: folder tuple and filename, and cumulative char costs
    file_data = []
    for parts in parsed:
        folder = tuple(parts[:-1])
        fn = parts[-1]
        file_data.append((folder, fn))
    
    # For efficiency, precompute prefix char sums for each file's folder
    # cost from depth l down to end of folder path
    # suffix_cost[file][l] = sum(len(folder[j])+1 for j in range(l, len(folder)))
    
    # Since folders can be large, let's precompute suffix sums
    file_suffix = []
    for (folder, fn) in file_data:
        suf = [0] * (len(folder) + 1)
        for i in range(len(folder)-1, -1, -1):
            suf[i] = suf[i+1] + len(folder[i]) + 1
        file_suffix.append(suf)
    
    min_cost = float('inf')
    
    for ref in folder_set:
        d = len(ref)
        total = 0
        for i, (folder, fn) in enumerate(file_data):
            k = len(folder)
            # find common prefix length
            l = 0
            max_l = min(d, k)
            while l < max_l and ref[l] == folder[l]:
                l += 1
            up_steps = d - l
            cost = up_steps * 3 + file_suffix[i][l] + len(fn)
            total += cost
        if total < min_cost:
            min_cost = total
    
    print(min_cost)

solve()