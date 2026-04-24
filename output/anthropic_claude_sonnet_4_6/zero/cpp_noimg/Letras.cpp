
#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin>>s;
    int cnt[26]={};
    for(char c:s) cnt[c-'A']++;
    int ans=0;
    for(int i=0;i<26;i++) ans+=cnt[i];
    cout<<ans<<endl;
}
