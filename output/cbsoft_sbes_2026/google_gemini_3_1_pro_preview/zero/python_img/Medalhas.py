import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t1 = int(input_data[0])
    t2 = int(input_data[1])
    t3 = int(input_data[2])
    
    swimmers = [(t1, 1), (t2, 2), (t3, 3)]
    swimmers.sort()
    
    for time, swimmer_id in swimmers:
        print(swimmer_id)

if __name__ == '__main__':
    main()