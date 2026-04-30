
D = int(input())
D -= 3
mod = D % 8
if mod == 0:
    print(2)
elif mod <= 2:
    print(1)
else:
    print(3)
