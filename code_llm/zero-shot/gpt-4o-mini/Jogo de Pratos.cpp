#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

const int MOD = 1e9 + 7;

long long mod_exp(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

long long max_pratos_after_spells(const vector<int>& a, const vector<int>& b, int K) {
    int N = a.size();
    vector<long long> max_effects(N);
    
    for (int i = 0; i < N; ++i) {
        max_effects[i] = (mod_exp(a[i], K, MOD) * (a[i] - 1) % MOD * mod_exp(a[i] - 1, K - 1, MOD) % MOD + b[i] * (mod_exp(a[i], K, MOD) - 1) % MOD * mod_exp(a[i] - 1, MOD - 2, MOD) % MOD) % MOD) % MOD;
    }
    
    return *max_element(max_effects.begin(), max_effects.end());
}

long long max_pratos_after_meals(long long x, const vector<int>& a, const vector<int>& b) {
    for (size_t i = 0; i < a.size(); ++i) {
        x = (x * a[i] + b[i]) % MOD;
    }
    return x;
}

int main() {
    int N, M, K;
    cin >> N >> M >> K;
    
    vector<int> a(N), b(N), a_prime(M), b_prime(M);
    for (int i = 0; i < N; ++i) cin >> a[i];
    for (int i = 0; i < N; ++i) cin >> b[i];
    for (int i = 0; i < M; ++i) cin >> a_prime[i];
    for (int i = 0; i < M; ++i) cin >> b_prime[i];
    
    long long max_spell_effect = max_pratos_after_spells(a, b, K);
    
    int Q;
    cin >> Q;
    vector<long long> results(Q);
    for (int i = 0; i < Q; ++i) {
        long long x;
        cin >> x;
        long long result = max_pratos_after_meals((x * max_spell_effect) % MOD, a_prime, b_prime);
        results[i] = result;
    }
    
    for (const auto& res : results) {
        cout << res << endl;
    }
    
    return 0;
}