import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    A = int(input_data[0])
    B = int(input_data[1])
    R = int(input_data[2])
    G = int(input_data[3])

    # Verifica se o diâmetro da pizza (2*R) cabe nas dimensões da caixa (A e B)
    # A pizza deve caber em ambas as dimensões.
    box_ok = (2 * R <= A) and (2 * R <= B)
    
    # Verifica se o ângulo G divide 360 graus exatamente, garantindo fatias iguais
    angle_ok = (360 % G == 0)
    
    if box_ok and angle_ok:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    solve()