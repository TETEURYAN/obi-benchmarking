import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])
P = list(map(int, input_data[2:]))
v = sorted(set(P))
m = len(v)
if m <= K:
    print(0)
else:
    freq = [P.count(x) for x in v]
    groups = list(zip(v, freq))
    costs = [(groups[i+1][0] - groups[i][0]) * groups[i][1] for i in range(m-1)]
    total_cost = 0
    while len(groups) > K:
        min_idx = costs.index(min(costs))
        total_cost += costs[min_idx]
        new_alt = groups[min_idx+1][0]
        new_freq = groups[min_idx][1] + groups[min_idx+1][1]
        groups[min_idx] = (new_alt, new_freq)
        del groups[min_idx+1]
        new_costs = []
        for k in range(len(groups)-1):
            if k < min_idx:
                new_costs.append(costs[k])
            elif k == min_idx:
                if min_idx + 1 < len(groups):
                    new_cost = (groups[min_idx+1][0] - groups[min_idx][0]) * groups[min_idx][1]
                    new_costs.append(new_cost)
            else:
                new_costs.append(costs[k])
        costs = new_costs
    print(total_cost)