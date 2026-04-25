#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    unordered_map<int,char> letter;
    unordered_map<int,int> nxt;
    for(int i=0;i<n;i++){
        int e,d;
        char c;
        cin >> e >> c >> d;
        letter[e]=c;
        nxt[e]=d;
    }
    string res;
    int cur=0;
    while(true){
        res+=letter[cur];
        int d=nxt[cur];
        if(d==1) break;
        cur=d;
    }
    cout << res << "\n";
    return 0;
}