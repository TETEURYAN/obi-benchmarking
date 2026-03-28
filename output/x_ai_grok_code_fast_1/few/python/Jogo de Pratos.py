import sys

input_data = sys.stdin.read().split()

idx = 0

N = int(input_data[idx])

idx +=1

M = int(input_data[idx])

idx +=1

K = int(input_data[idx])

idx +=1

a = []

for _ in range(N):

 a.append(int(input_data[idx]))

 idx +=1

b = []

for _ in range(N):

 b.append(int(input_data[idx]))

 idx +=1

a_prime = []

for _ in range(M):

 a_prime.append(int(input_data[idx]))

 idx +=1

b_prime = []

for _ in range(M):

 b_prime.append(int(input_data[idx]))

 idx +=1

Q = int(input_data[idx])

idx +=1

x_list = []

for _ in range(Q):

 x_list.append(int(input_data[idx]))

 idx +=1

MOD = 10**9 + 7

# find best feitiço

if N == 0:

 A_f = 1

 B_f = 0

else:

 best_i = 0

 for i in range(1, N):

  if a[i] > a[best_i] or (a[i] == a[best_i] and b[i] > b[best_i]):

   best_i = i

 a_best = a[best_i]

 b_best = b[best_i]

 if K == 0:

  A_f = 1

  B_f = 0

 else:

  A_f = pow(a_best, K, MOD)

  if a_best == 1:

   B_f = K * b_best % MOD

  else:

   inv = pow(a_best - 1, MOD - 2, MOD)

   B_f = b_best * (A_f - 1) * inv % MOD

# for refeições

ref = list(zip(a_prime, b_prime))

ref.sort(key=lambda x: -x[1])

A_r = 1

B_r = 0

for aa, bb in ref:

 A_r = A_r * aa % MOD

 B_r = (B_r * aa + bb) % MOD

# now for each x

for x in x_list:

 x_prime = (A_f * x + B_f) % MOD

 final = (A_r * x_prime + B_r) % MOD

 print(final)