#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

long long pow_mod(long long base, long long exp, long long mod) {
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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;

    vector<long long> feitiços_a(N), feitiços_b(N);
    for (int i = 0; i < N; i++) cin >> feitiços_a[i];
    for (int i = 0; i < N; i++) cin >> feitiços_b[i];

    vector<long long> refeições_a(M), refeições_b(M);
    for (int i = 0; i < M; i++) cin >> refeições_a[i];
    for (int i = 0; i < M; i++) cin >> refeições_b[i];

    vector<long long> max_feiticos(K + 1, 0);
    for (int i = 0; i < N; i++) {
        long long a = feitiços_a[i], b = feitiços_b[i];
        if (a == 1) {
            for (int k = 1; k <= K; k++) {
                max_feiticos[k] = (max_feiticos[k] + b) % MOD;
            }
        } else {
            long long ak = 1, sum = 0;
            for (int k = 0; k <= K; k++) {
                if (k > 0) {
                    ak = (ak * a) % MOD;
                    sum = (sum + (ak * b) % MOD) % MOD;
                }
                max_feiticos[k] = (max_feiticos[k] + sum) % MOD;
            }
        }
    }

    vector<pair<long long, long long>> refeições;
    for (int i = 0; i < M; i++) {
        refeições.emplace_back(refeições_a[i], refeições_b[i]);
    }
    sort(refeições.begin(), refeições.end(), [](const auto &lhs, const auto &rhs) {
        return lhs.first > rhs.first;
    });

    int Q;
    cin >> Q;
    vector<long long> x(Q);
    for (int i = 0; i < Q; i++) cin >> x[i];

    for (int i = 0; i < Q; i++) {
        long long result = 0;
        for (int k = 0; k <= K; k++) {
            long long current = (max_feiticos[k] * x[i]) % MOD;
            for (const auto &refeição : refeições) {
                current = (refeição.first * current + refeição.second) % MOD;
            }
            result = max(result, current);
        }
        cout << result << endl;
    }

    return 0;
}