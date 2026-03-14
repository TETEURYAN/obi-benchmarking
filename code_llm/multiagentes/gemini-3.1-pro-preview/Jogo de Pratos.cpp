#include <bits/stdc++.h>

using namespace std;

const long long MOD = 1000000007;

struct Spell {
    long long a, b;
};

struct Meal {
    long long a, b;
};

struct Query {
    long long x;
    int id;
};

struct Line {
    long long m, c;
};

bool compMeal(const Meal& m1, const Meal& m2) {
    long long v1 = m1.b * (m2.a - 1);
    long long v2 = m2.b * (m1.a - 1);
    if (v1 != v2) return v1 > v2;
    if (m1.a != m2.a) return m1.a > m2.a;
    return m1.b > m2.b;
}

bool compSpell(const Spell& s1, const Spell& s2) {
    if (s1.a != s2.a) return s1.a < s2.a;
    return s1.b < s2.b;
}

bool bad(Line l1, Line l2, Line l3) {
    long long num1 = l1.c - l2.c;
    long long den1 = l2.m - l1.m;
    long long num2 = l2.c - l3.c;
    long long den2 = l3.m - l2.m;
    return num1 * den2 >= num2 * den1;
}

bool better_or_equal(Line l1, Line l2, long long x) {
    return l1.m * x + l1.c <= l2.m * x + l2.c;
}

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    long long K;
    if (!(cin >> N >> M >> K)) return 0;

    vector<Spell> spells(N);
    for (int i = 0; i < N; i++) cin >> spells[i].a;
    for (int i = 0; i < N; i++) cin >> spells[i].b;

    vector<Meal> meals(M);
    for (int i = 0; i < M; i++) cin >> meals[i].a;
    for (int i = 0; i < M; i++) cin >> meals[i].b;

    int Q;
    cin >> Q;
    vector<Query> queries(Q);
    for (int i = 0; i < Q; i++) {
        cin >> queries[i].x;
        queries[i].id = i;
    }

    sort(meals.begin(), meals.end(), compMeal);
    long long A_meal = 1;
    long long B_meal = 0;
    for (int i = 0; i < M; i++) {
        A_meal = (A_meal * meals[i].a) % MOD;
        B_meal = (B_meal * meals[i].a + meals[i].b) % MOD;
    }

    Spell S_max = spells[0];
    for (int i = 1; i < N; i++) {
        if (spells[i].a > S_max.a) {
            S_max = spells[i];
        } else if (spells[i].a == S_max.a && spells[i].b > S_max.b) {
            S_max = spells[i];
        }
    }

    sort(spells.begin(), spells.end(), compSpell);
    vector<Line> hull;
    for (int i = 0; i < N; i++) {
        Line l = {spells[i].a, spells[i].b};
        if (!hull.empty() && hull.back().m == l.m) {
            hull.pop_back();
        }
        while (hull.size() >= 2 && bad(hull[hull.size() - 2], hull.back(), l)) {
            hull.pop_back();
        }
        hull.push_back(l);
    }

    sort(queries.begin(), queries.end(), [](const Query& q1, const Query& q2) {
        return q1.x < q2.x;
    });

    vector<long long> ans(Q);
    int ptr = 0;
    for (int i = 0; i < Q; i++) {
        long long x = queries[i].x;
        
        while (ptr + 1 < (int)hull.size() && better_or_equal(hull[ptr], hull[ptr + 1], x)) {
            ptr++;
        }

        long long best_a = hull[ptr].m;
        long long best_b = hull[ptr].c;

        long long X1 = ((best_a % MOD) * (x % MOD) + (best_b % MOD)) % MOD;
        long long X_after = X1;

        if (K > 1) {
            long long A_max = S_max.a;
            long long B_max = S_max.b;
            if (A_max == 1) {
                long long add = ((K - 1) % MOD) * (B_max % MOD) % MOD;
                X_after = (X1 + add) % MOD;
            } else {
                long long p = power(A_max, K - 1);
                long long term1 = (X1 * p) % MOD;
                long long num = (p - 1 + MOD) % MOD;
                long long den = modInverse(A_max - 1);
                long long term2 = (B_max % MOD) * num % MOD * den % MOD;
                X_after = (term1 + term2) % MOD;
            }
        }

        long long final_ans = ((X_after * A_meal) % MOD + B_meal) % MOD;
        ans[queries[i].id] = final_ans;
    }

    for (int i = 0; i < Q; i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}