
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
using namespace std;

const int MOD = 1e9 + 7;

long long maxPlatesAfterSpells(long long x, const vector<int>& a, const vector<int>& b, int K) {
    long long max_a = 0, max_b = 0;
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] > max_a) {
            max_a = a[i];
            max_b = b[i];
        } else if (a[i] == max_a) {
            max_b = max(max_b, b[i]);
        }
    }
    long long result = x;
    for (int i = 0; i < K; ++i) {
        result = (result * max_a + max_b) % MOD;
    }
    return result;
}

long long maxPlatesAfterMeals(long long x, const vector<int>& a, const vector<int>& b) {
    long long result = x;
    for (int i = 0; i < a.size(); ++i) {
        result = (result * a[i] + b[i]) % MOD;
    }
    return result;
}

int main() {
    int N, M, K;
    cin >> N >> M >> K;
    vector<int> a(N), b(N), a_prime(M), b_prime(M);
    for (int i = 0; i < N; ++i) cin >> a[i];
    for (int i = 0; i < N; ++i) cin >> b[i];
    for (int i = 0; i < M; ++i) cin >> a_prime[i];
    for (int i = 0; i < M; ++i) cin >> b_prime[i];
    
    int Q;
    cin >> Q;
    vector<long long> x(Q);
    for (int i = 0; i < Q; ++i) cin >> x[i];

    long long max_after_spells = maxPlatesAfterSpells(1, a, b, K);
    long long max_after_meals = maxPlatesAfterMeals(max_after_spells, a_prime, b_prime);

    for (int i = 0; i < Q; ++i) {
        long long result = maxPlatesAfterMeals(maxPlatesAfterSpells(x[i], a, b, K), a_prime, b_prime);
        cout << result << endl;
    }
    return 0;
}
