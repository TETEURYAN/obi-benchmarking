
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int>a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    int cnt=0;
    for(int i=0;i+2<n;i++){
        if(a[i]==1&&a[i+1]==0&&a[i+2]==0) cnt++;
    }
    cout<<cnt<<endl;
}
