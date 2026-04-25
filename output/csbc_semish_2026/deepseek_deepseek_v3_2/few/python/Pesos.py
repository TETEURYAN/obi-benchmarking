
import sys

def possible(weights):
    n = len(weights)
    # State: can we have weight difference d? (d is absolute difference)
    # Actually we just need to track if it's feasible.
    # We can think greedily: always try to pair heaviest with lightest possible.
    left = 0
    right = n - 1
    last_up = 0  # weight currently in upper cabin (second floor)
    
    while left <= right:
        # Try to move heaviest box first
        if weights[right] - last_up <= 8:
            # Move heaviest box up alone (empty cabin down)
            last_up = weights[right]
            right -= 1
        else:
            # Need to pair two boxes: heaviest and some lighter
            if left == right:
                # Only one box left and it's too heavy alone
                return False
            if weights[right] - weights[left] <= 8:
                # Move heaviest up, lightest down together
                last_up = weights[right]
                right -= 1
                left += 1
            else:
                # No pairing works
                return False
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    weights = list(map(int, data[1:]))
    if possible(weights):
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
