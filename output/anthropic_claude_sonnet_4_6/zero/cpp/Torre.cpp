
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    scanf("%d",&n);
    vector<vector<int>> g(n,vector<int>(n));
    vector<long long> row(n,0),col(n,0);
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            scanf("%d",&g[i][j]);
            row[i]+=g[i][j];
            col[j]+=g[i][j];
        }
    long long ans=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            long long w=row[i]+col[j]-g[i][j];
            if(w>ans) ans=w;
        }
    printf("%lld\n",ans);
}
