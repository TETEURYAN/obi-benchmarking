
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    scanf("%d",&n);
    unordered_map<int,pair<char,int>> mp;
    for(int i=0;i<n;i++){
        int e,d;
        char c;
        scanf("%d %c %d",&e,&c,&d);
        mp[e]={c,d};
    }
    int cur=0;
    string res="";
    while(mp.count(cur)){
        auto [c,d]=mp[cur];
        res+=c;
        cur=d;
    }
    printf("%s\n",res.c_str());
}
