import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split('\n')
    idx = 0
    N = int(input_data[idx]); idx += 1
    
    files = []
    for i in range(N):
        line = input_data[idx].strip(); idx += 1
        files.append(line)
    
    # Parse each file into path components
    # path_parts[i] = list of folder names + filename
    parsed = []
    for f in files:
        parts = f.split('/')
        parsed.append(parts)
    
    # Build tree of folders
    # We need to find all unique folder paths (nodes in the tree)
    # For each possible reference folder, compute total catalog length
    
    # A folder is identified by its path from root (list of folder names)
    # Root is represented as empty tuple ()
    
    # Collect all folder nodes
    folder_set = set()
    folder_set.add(())  # root
    
    for parts in parsed:
        # folders are all prefixes except the last element (which is the file)
        for i in range(len(parts) - 1):
            folder_set.add(tuple(parts[:i+1]))
    
    # For each file and each reference folder, compute the description length
    # Description of file given reference folder ref_path:
    # file_path = parts (list), file is parts[-1], folder of file is parts[:-1]
    # ref_path = tuple of folder names
    
    # Find LCA of file_folder and ref_path
    # depth of ref = len(ref_path)
    # depth of file_folder = len(parts) - 1
    # LCA depth = length of common prefix
    
    # ups = depth(ref) - depth(LCA)  -> number of '../' needed
    # downs = file_folder path from LCA to file_folder
    # description = '../' * ups + '/'.join(downs_parts + [filename])
    # length = 3*ups + sum(len(p)+1 for p in downs_parts) + len(filename)
    # if downs_parts is empty and ups == 0: just filename length
    # if downs_parts not empty: len('/'.join(downs_parts)) + 1 (for /) + len(filename)
    
    # For efficiency, precompute for each file:
    # file_folder = tuple(parts[:-1])
    # filename = parts[-1]
    
    # For a given reference ref (tuple):
    # lca_len = length of common prefix between ref and file_folder
    # ups = len(ref) - lca_len
    # down_parts = file_folder[lca_len:]  (tuple slice)
    # length = 3*ups + sum(len(p)+1 for p in down_parts) + len(filename)
    # but if ups==0 and len(down_parts)==0: just len(filename)
    # else if ups==0: sum(len(p)+1 for p in down_parts) + len(filename)
    # general: 3*ups + sum(len(p)+1 for p in down_parts) + len(filename)
    # Note: when down_parts is empty and ups==0, formula gives len(filename) correct
    # when down_parts not empty: each part contributes len(p)+1 (for the '/' after it)
    # filename doesn't have '/' after, so total = 3*ups + sum(len(p)+1 for p in down_parts) + len(filename)
    # This works because down_parts[0] has no leading '/', but the formula counts '/' after each down part
    # Actually let's verify: ref=Caetano=('MPB','Caetano'), file=MPB/Cartola/Alvorada.mp3
    # file_folder=('MPB','Cartola'), filename='Alvorada.mp3'
    # lca=('MPB',) len=1, ups=2-1=1, down_parts=('Cartola',)
    # length = 3*1 + (7+1) + 12 = 3+8+12=23, actual '../Cartola/Alvorada.mp3'=23 chars. Correct!
    
    file_info = []
    for parts in parsed:
        file_folder = tuple(parts[:-1])
        filename = parts[-1]
        # precompute prefix sums of (len+1) for file_folder
        file_info.append((file_folder, filename))
    
    # For each folder in folder_set, compute total length
    best = float('inf')
    
    for ref in folder_set:
        ref_len = len(ref)
        total = 0
        for (file_folder, filename) in file_info:
            ff_len = len(file_folder)
            # compute lca length
            lca_len = 0
            min_len = min(ref_len, ff_len)
            for k in range(min_len):
                if ref[k] == file_folder[k]:
                    lca_len += 1
                else:
                    break
            ups = ref_len - lca_len
            down_parts = file_folder[lca_len:]
            length = 3 * ups + sum(len(p) + 1 for p in down_parts) + len(filename)
            total += length
        if total < best:
            best = total
    
    print(best)

solve()