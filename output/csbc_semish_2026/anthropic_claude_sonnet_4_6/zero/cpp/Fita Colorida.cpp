
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    
    vector<int> dist(n, INT_MAX);
    
    // BFS from all 0s
    deque<int> q;
    for(int i=0;i<n;i++){
        if(a[i]==0){
            dist[i]=0;
            q.push_back(i);
        }
    }
    
    while(!q.empty()){
        int cur=q.front(); q.pop_front();
        if(cur-1>=0 && dist[cur-1]==INT_MAX){
            dist[cur-1]=dist[cur]+1;
            q.push_back(cur-1);
        }
        if(cur+1<n && dist[cur+1]==INT_MAX){
            dist[cur+1]=dist[cur]+1;
            q.push_back(cur+1);
        }
    }
    
    for(int i=0;i<n;i++){
        if(i) cout<<" ";
        cout<<min(dist[i],9);
    }
    cout<<endl;
}
