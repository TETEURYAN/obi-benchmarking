s = input().strip()

mp = {}
for ch in "ABC":
    mp[ch] = "2"
for ch in "DEF":
    mp[ch] = "3"
for ch in "GHI":
    mp[ch] = "4"
for ch in "JKL":
    mp[ch] = "5"
for ch in "MNO":
    mp[ch] = "6"
for ch in "PQRS":
    mp[ch] = "7"
for ch in "TUV":
    mp[ch] = "8"
for ch in "WXY":
    mp[ch] = "9"

print("".join(ch if ch == "-" else mp[ch] for ch in s))