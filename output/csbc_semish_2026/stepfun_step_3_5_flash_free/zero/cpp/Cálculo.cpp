#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;
    vector<int> X(M), Y(N);
    for (int i = 0; i < M; i++) cin >> X[i];
    for (int i = 0; i < N; i++) cin >> Y[i];
    int L = max(M, N);
    vector<int> A(L, 0), B(L, 0);
    for (int i = 0; i < M; i++) A[i] = X[i];
    for (int i = 0; i < N; i++) B[i] = Y[i];
    vector<int> R(L);
    int carry = 0;
    for (int i = L - 1; i >= 0; i--) {
        int soma = A[i] + B[i] + carry;
        R[i] = soma % 2;
        carry = soma / 2;
    }
    int last = -1;
    for (int i = L - 1; i >= 0; i--) {
        if (R[i] == 1) {
            last = i;
            break;
        }
    }
    if (last == -1) {
        cout << 0;
    } else {
        for (int i = 0; i <= last; i++) {
            if (i > 0) cout << " ";
            cout << R[i];
        }
    }
    cout << endl;
    return 0;
}