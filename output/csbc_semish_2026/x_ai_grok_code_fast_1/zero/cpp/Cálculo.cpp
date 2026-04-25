
#include <bits/stdc++.h>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;
    vector<int> X(M);
    for(int i = 0; i < M; i++) cin >> X[i];
    vector<int> Y(N);
    for(int i = 0; i < N; i++) cin >> Y[i];
    int len = max(M, N);
    vector<int> result(len + 1, 0);
    int carry = 0;
    for(int i = len - 1; i >= 0; i--) {
        int bitX = (i < M) ? X[i] : 0;
        int bitY = (i < N) ? Y[i] : 0;
        int sum = bitX + bitY + carry;
        result[i + 1] = sum % 2;
        carry = sum / 2;
    }
    if(carry) result[0] = carry;
    int last = len;
    while(last >= 1 && result[last] == 0) last--;
    for(int i = 1; i <= last; i++) {
        cout << result[i];
        if(i < last) cout << " ";
        else cout << "\n";
    }
    return 0;
}
