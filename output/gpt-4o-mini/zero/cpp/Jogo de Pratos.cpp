
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

long long max_pratos(long long x, const vector<int>& a, const vector<int>& b, int K) {
    long long max_a = 1, max_b = 0;
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] > max_a) {
            max_a = a[i];
            max_b = b[i];
        } else if (a[i] == max_a) {
            max_b = max(max_b, b[i]);
        }
    }
    
    long long total_multiplier = mod_exp(max_a, K, MOD);
    long long total_addition = (max_b * (total_multiplier - 1 + MOD) % MOD * mod_exp(max_a - 1, MOD - 2, MOD)) % MOD;
    
    return (total_multiplier * x % MOD + total_addition) % MOD;
}

long long calculate_final(long long x, const vector<int>& a, const vector<int>& b, const vector<int>& a_prime, const vector<int>& b_prime, int K) {
    long long after_spells = max_pratos(x, a, b, K);
    
    long long max_a_prime = *max_element(a_prime.begin(), a_prime.end());
    long long max_b_prime = 0;
    for (int i = 0; i < a_prime.size(); ++i) {
        if (a_prime[i] == max_a_prime) {
            max_b_prime = max(max_b_prime, b_prime[i]);
        }
    }
    
    return (max_a_prime * after_spells % MOD + max_b_prime) % MOD;
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
    
    for (int i = 0; i < Q; ++i) {
        cout << calculate_final(x[i], a, b, a_prime, b_prime, K) << endl;
    }
    
    return 0;
}
