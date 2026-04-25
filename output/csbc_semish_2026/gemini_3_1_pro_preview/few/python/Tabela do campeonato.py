import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

g_J, g_P, g_V, g_E, g_D = map(int, input_data)

v_start = g_V if g_V != -1 else 0
v_end = g_V if g_V != -1 else 100

e_start = g_E if g_E != -1 else 0
e_end = g_E if g_E != -1 else 100

d_start = g_D if g_D != -1 else 0
d_end = g_D if g_D != -1 else 100

for v in range(v_start, v_end + 1):
    for e in range(e_start, e_end + 1):
        for d in range(d_start, d_end + 1):
            j = v + e + d
            p = 3 * v + e
            
            if (g_J == -1 or g_J == j) and (g_P == -1 or g_P == p):
                print(f"{j} {p} {v} {e} {d}")
                sys.exit()