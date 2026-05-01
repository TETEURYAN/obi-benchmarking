import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    l = int(input_data[1])
    
    # Adjust to 0-based index for easier calculation
    k -= 1
    l -= 1
    
    if k // 8 == l // 8:
        # Same half of the bracket (positions 1-8 or 9-16)
        if k // 4 == l // 4:
            # Same quarter (e.g., 1-4, 5-8)
            if k // 2 == l // 2:
                # Same pair (e.g., 1-2, 3-4)
                print("oitavas")
            else:
                print("quartas")
        else:
            print("semifinal")
    else:
        print("final")

if __name__ == "__main__":
    solve()