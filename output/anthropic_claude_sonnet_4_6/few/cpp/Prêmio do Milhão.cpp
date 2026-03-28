#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    long long sum=0;
    for(int i=1;i<=n;i++){
        long long a;
        cin>>a;
        sum+=a;
        if(sum>=1000000){
            cout<<i<<endl;
            return 0;
        }
    }
    return 0;
}