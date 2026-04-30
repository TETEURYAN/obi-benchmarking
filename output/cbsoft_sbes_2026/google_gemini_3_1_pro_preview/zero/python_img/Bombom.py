import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 7:
        return
    
    dominant_suit = input_data[0][1]
    
    base_values = {
        'A': 10,
        'J': 11,
        'Q': 12,
        'K': 13
    }
    
    def get_value(card):
        val = base_values[card[0]]
        if card[1] == dominant_suit:
            val += 4
        return val
        
    luana_score = sum(get_value(card) for card in input_data[1:4])
    edu_score = sum(get_value(card) for card in input_data[4:7])
    
    if luana_score > edu_score:
        print("Luana")
    elif edu_score > luana_score:
        print("Edu")
    else:
        print("empate")

if __name__ == '__main__':
    solve()