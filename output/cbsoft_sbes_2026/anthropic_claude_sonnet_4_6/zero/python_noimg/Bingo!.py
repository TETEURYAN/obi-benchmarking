import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    U = int(input_data[idx]); idx += 1
    
    cartelas = []
    for i in range(N):
        nums = set()
        for j in range(K):
            nums.add(int(input_data[idx])); idx += 1
        cartelas.append(nums)
    
    sequence = []
    for i in range(U):
        sequence.append(int(input_data[idx])); idx += 1
    
    # For each card, find when it gets completed
    # completion time = index (1-based) of the last number drawn that completes the card
    # = max position in sequence of each number in the card
    
    # Build position map
    pos = {}
    for i, num in enumerate(sequence):
        pos[num] = i + 1  # 1-based position
    
    completion_times = []
    for i, card in enumerate(cartelas):
        t = max(pos[num] for num in card)
        completion_times.append(t)
    
    min_time = min(completion_times)
    winners = [i + 1 for i, t in enumerate(completion_times) if t == min_time]
    
    print(' '.join(map(str, winners)))

main()