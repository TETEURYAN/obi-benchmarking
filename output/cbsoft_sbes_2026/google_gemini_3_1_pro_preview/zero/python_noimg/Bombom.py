import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    dominant_suit = input_data[0][1]
    
    def get_value(card):
        fig = card[0]
        suit = card[1]
        
        if fig == 'A':
            val = 10
        elif fig == 'J':
            val = 11
        elif fig == 'Q':
            val = 12
        elif fig == 'K':
            val = 13
        else:
            val = 0
            
        if suit == dominant_suit:
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