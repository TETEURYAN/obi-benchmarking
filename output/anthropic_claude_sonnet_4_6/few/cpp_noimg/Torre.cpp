#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<vector<long long>> g(n, vector<long long>(n));
    vector<long long> rowsum(n,0), colsum(n,0);
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            cin >> g[i][j];
            rowsum[i]+=g[i][j];
            colsum[j]+=g[i][j];
        }
    long long ans = LLONG_MIN;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            long long w = rowsum[i]+colsum[j]-g[i][j];
            if(w>ans) ans=w;
        }
    cout << ans << endl;
    return 0;
}