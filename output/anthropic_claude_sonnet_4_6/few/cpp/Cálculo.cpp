#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int M, N;
    cin >> M >> N;
    vector<int> X(M), Y(N);
    for(int i=0;i<M;i++) cin>>X[i];
    for(int i=0;i<N;i++) cin>>Y[i];
    int maxLen = max(M,N);
    // pad to same length
    vector<int> A(maxLen,0), B(maxLen,0);
    for(int i=0;i<M;i++) A[i]=X[i];
    for(int i=0;i<N;i++) B[i]=Y[i];
    // add from right to left
    vector<int> res(maxLen,0);
    int carry=0;
    for(int i=maxLen-1;i>=0;i--){
        int s=A[i]+B[i]+carry;
        res[i]=s%2;
        carry=s/2;
    }
    // carry should be 0 since X+Y<1
    // remove trailing zeros
    int last=maxLen-1;
    while(last>0 && res[last]==0) last--;
    for(int i=0;i<=last;i++){
        if(i>0) cout<<" ";
        cout<<res[i];
    }
    cout<<endl;
    return 0;
}