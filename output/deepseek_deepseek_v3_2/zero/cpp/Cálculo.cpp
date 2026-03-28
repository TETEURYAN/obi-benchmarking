
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
    
    int max_len = max(M, N);
    vector<int> result(max_len + 1, 0);
    
    int carry = 0;
    for (int i = 0; i < max_len; i++) {
        int bit_sum = carry;
        if (i < M) bit_sum += X[M - 1 - i];
        if (i < N) bit_sum += Y[N - 1 - i];
        
        result[max_len - i] = bit_sum % 2;
        carry = bit_sum / 2;
    }
    result[0] = carry;
    
    int start = 0;
    while (start < result.size() && result[start] == 0) {
        start++;
    }
    
    if (start == result.size()) {
        cout << "0" << endl;
        return 0;
    }
    
    for (int i = start; i < result.size(); i++) {
        cout << result[i];
        if (i != result.size() - 1) cout << " ";
    }
    cout << endl;
    
    return 0;
}
