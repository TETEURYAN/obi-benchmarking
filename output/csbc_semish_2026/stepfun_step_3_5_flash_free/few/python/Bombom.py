import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    cartas = data[:7]
    dominante = cartas[0][1]
    
    def valor(figura, naipe):
        base = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}[figura]
        return base + 4 if naipe == dominante else base
    
    soma_luana = sum(valor(c[0], c[1]) for c in cartas[1:4])
    soma_edu = sum(valor(c[0], c[1]) for c in cartas[4:7])
    
    if soma_luana > soma_edu:
        print("Luana")
    elif soma_edu > soma_luana:
        print("Edu")
    else:
        print("empate")

if __name__ == "__main__":
    main()