import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A = int(input_data[0])
    B = int(input_data[1])
    
    ana = A % 3
    beatriz = B % 3
    
    if beatriz == ana:
        beatriz = (beatriz + 1) % 3
        
    carolina = 3 - ana - beatriz
    print(carolina)

if __name__ == '__main__':
    main()