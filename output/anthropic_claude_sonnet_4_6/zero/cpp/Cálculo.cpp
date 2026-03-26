
#include<bits/stdc++.h>
using namespace std;

int main(){
    int M, N;
    cin >> M >> N;
    
    vector<int> X(M), Y(N);
    for(int i = 0; i < M; i++) cin >> X[i];
    for(int i = 0; i < N; i++) cin >> Y[i];
    
    int maxLen = max(M, N);
    
    // Extend both to maxLen
    vector<int> A(maxLen, 0), B(maxLen, 0);
    for(int i = 0; i < M; i++) A[i] = X[i];
    for(int i = 0; i < N; i++) B[i] = Y[i];
    
    // Result can be at most maxLen+1 digits (but X+Y < 1, so no overflow beyond)
    // Actually since X+Y < 1, the result fits in maxLen+1 bits at most
    vector<int> res(maxLen + 1, 0);
    
    int carry = 0;
    for(int i = maxLen - 1; i >= 0; i--){
        int s = A[i] + B[i] + carry;
        res[i + 1] = s % 2;
        carry = s / 2;
    }
    res[0] = carry;
    
    // Find the actual length needed (remove trailing zeros, but keep at least one digit)
    // Also remove leading zeros if any (res[0] should be 0 since X+Y < 1)
    // Find last 1
    int last = -1;
    for(int i = maxLen; i >= 0; i--){
        if(res[i] == 1){ last = i; break; }
    }
    
    // Find first non-zero (should start from index 0 or 1)
    // Since X+Y < 1, res[0] = 0
    // Output from index 0 to last (but skip leading... wait, obi-2015 uses minimum digits)
    // The representation starts from position 1 (2^-1), so res[0] corresponds to 2^0 which should be 0
    // We output from index 1 (first fractional bit) to last
    // But wait, if res[0] = 0, we start from index 1
    // Actually res[i] at position i corresponds to 2^(-i) for i>=1, and 2^0 for i=0
    // Since X+Y < 1, res[0] = 0
    
    // Output from index 1 to last
    if(last <= 0){
        // This shouldn't happen since X,Y > 0
        cout << 0 << endl;
    } else {
        for(int i = 1; i <= last; i++){
            if(i > 1) cout << " ";
            cout << res[i];
        }
        cout << endl;
    }
    
    return 0;
}
