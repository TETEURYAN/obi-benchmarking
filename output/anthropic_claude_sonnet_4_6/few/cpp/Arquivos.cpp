#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    long long b;
    cin >> n >> b;
    vector<long long> a(n);
    for(int i=0;i<n;i++) cin >> a[i];
    sort(a.begin(),a.end());
    int lo=0, hi=n-1, folders=0;
    while(lo<=hi){
        if(lo==hi){
            folders++;
            break;
        }
        if(a[lo]+a[hi]<=b){
            folders++;
            lo++;
            hi--;
        } else {
            folders++;
            hi--;
        }
    }
    cout << folders << endl;
    return 0;
}