
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string S;
    cin >> S;
    
    // dp[i] = tamanho da maior subsequência crescente que termina com a letra i
    // onde i é índice 0 para 'A', 1 para 'B', ... 25 para 'Z'
    vector<int> dp(26, 0);
    
    for (char c : S) {
        int idx = c - 'A';
        int best = 0;
        // Procura a melhor subsequência que termina com letra <= c
        for (int i = 0; i <= idx; i++) {
            best = max(best, dp[i]);
        }
        dp[idx] = best + 1;
    }
    
    int ans = 0;
    for (int i = 0; i < 26; i++) {
        ans = max(ans, dp[i]);
    }
    
    cout << ans << endl;
    
    return 0;
}
