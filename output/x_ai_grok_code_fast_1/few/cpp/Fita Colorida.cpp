#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> a(N);
    for(int i = 0; i < N; i++) cin >> a[i];
    vector<int> dist(N, INT_MAX);
    for(int i = 0; i < N; i++) {
        if(a[i] == 0) dist[i] = 0;
    }
    // left to right
    for(int i = 1; i < N; i++) {
        dist[i] = min(dist[i], dist[i-1] + 1);
    }
    // right to left
    for(int i = N-2; i >= 0; i--) {
        dist[i] = min(dist[i], dist[i+1] + 1);
    }
    // output
    for(int i = 0; i < N; i++) {
        int val = min(dist[i], 9);
        cout << val;
        if(i < N-1) cout << " ";
        else cout << "\n";
    }
    return 0;
}