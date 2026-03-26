
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int M, N;
    if (!(cin >> M >> N)) return 0;
    
    vector<int> X(M);
    for (int i = 0; i < M; ++i) {
        cin >> X[i];
    }
    
    vector<int> Y(N);
    for (int i = 0; i < N; ++i) {
        cin >> Y[i];
    }
    
    int L = max(M, N);
    X.resize(L, 0);
    Y.resize(L, 0);
    
    vector<int> ans(L);
    int carry = 0;
    for (int i = L - 1; i >= 0; --i) {
        int sum = X[i] + Y[i] + carry;
        ans[i] = sum % 2;
        carry = sum / 2;
    }
    
    int last_one = -1;
    for (int i = L - 1; i >= 0; --i) {
        if (ans[i] == 1) {
            last_one = i;
            break;
        }
    }
    
    for (int i = 0; i <= last_one; ++i) {
        cout << ans[i] << (i == last_one ? "" : " ");
    }
    cout << "\n";
    
    return 0;
}
