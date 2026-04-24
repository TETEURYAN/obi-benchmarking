
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<vector<int>> grid(n, vector<int>(n));
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            cin >> grid[i][j];
    
    vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
    deque<pair<int,int>> dq;
    dist[0][0] = 0;
    dq.push_front({0,0});
    
    int dx[] = {0,0,1,-1};
    int dy[] = {1,-1,0,0};
    
    while(!dq.empty()){
        auto [x,y] = dq.front();
        dq.pop_front();
        for(int d = 0; d < 4; d++){
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
            int cost = dist[x][y] + grid[nx][ny];
            if(cost < dist[nx][ny]){
                dist[nx][ny] = cost;
                if(grid[nx][ny] == 0)
                    dq.push_front({nx,ny});
                else
                    dq.push_back({nx,ny});
            }
        }
    }
    
    cout << dist[n-1][n-1] << endl;
    return 0;
}
