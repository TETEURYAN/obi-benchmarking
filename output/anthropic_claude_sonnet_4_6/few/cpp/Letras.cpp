#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    // Count occurrences of each letter, then sum all counts
    // A non-decreasing subsequence: we can pick all occurrences of each letter
    // that appears, since same letters are allowed (non-decreasing = next >= prev)
    // So the answer is: for each letter that appears, count how many times it appears
    // and sum them all = length of s minus... wait, no.
    // Actually a "crescente" (non-decreasing) subsequence allows repeated letters.
    // The longest non-decreasing subsequence of a string over alphabet {A..Z}:
    // We can use DP with patience sorting style.
    // But actually: since alphabet is only 26 letters, we can do it in O(26*N).
    // dp[c] = length of longest non-decreasing subsequence ending with letter c
    // For each character ch in s:
    //   dp[ch] = max(dp[a] for a <= ch) + 1
    // Answer = max(dp[c]) for all c
    
    vector<long long> dp(26, 0);
    for(char c : s){
        int idx = c - 'A';
        long long best = 0;
        for(int j = 0; j <= idx; j++){
            best = max(best, dp[j]);
        }
        dp[idx] = max(dp[idx], best + 1);
    }
    long long ans = *max_element(dp.begin(), dp.end());
    cout << ans << endl;
    return 0;
}