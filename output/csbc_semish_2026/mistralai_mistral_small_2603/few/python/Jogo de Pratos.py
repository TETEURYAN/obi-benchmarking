
import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1
    M = int(data[ptr]); ptr += 1
    K = int(data[ptr]); ptr += 1

    a_spells = list(map(int, data[ptr:ptr+N])); ptr += N
    b_spells = list(map(int, data[ptr:ptr+N])); ptr += N
    a_meals = list(map(int, data[ptr:ptr+M])); ptr += M
    b_meals = list(map(int, data[ptr:ptr+M])); ptr += M
    Q = int(data[ptr]); ptr += 1
    X = list(map(int, data[ptr:ptr+Q]))

    spells = list(zip(a_spells, b_spells))
    meals = list(zip(a_meals, b_meals))

    def get_best_spells(spells, K):
        spells.sort(key=lambda x: x[0], reverse=True)
        total_a = 1
        total_b = 0
        for a, b in spells:
            if K == 0:
                break
            if total_a * a + total_b > total_a + total_b:
                total_a = (total_a * a) % MOD
                total_b = (total_b * a + b) % MOD
                K -= 1
            else:
                break
        return total_a, total_b

    A_spell, B_spell = get_best_spells(spells, K)

    def get_best_meals(meals):
        meals.sort(key=lambda x: (x[0], x[1]), reverse=True)
        A_meal = 1
        B_meal = 0
        for a, b in meals:
            new_A = (A_meal * a) % MOD
            new_B = (A_meal * b + B_meal) % MOD
            if new_A > A_meal or (new_A == A_meal and new_B > B_meal):
                A_meal, B_meal = new_A, new_B
            else:
                break
        return A_meal, B_meal

    A_meal, B_meal = get_best_meals(meals)

    def apply_effect(x, A, B):
        return (x * A + B) % MOD

    results = []
    for x in X:
        x_mod = x % MOD
        res = apply_effect(x_mod, A_spell, B_spell)
        res = apply_effect(res, A_meal, B_meal)
        results.append(str(res))

    print('\n'.join(results))

if __name__ == "__main__":
    main()
