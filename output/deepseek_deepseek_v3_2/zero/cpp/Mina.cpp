
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

struct State {
    int x, y, cost;
    State(int _x, int _y, int _cost) : x(_x), y(_y), cost(_cost) {}
    bool operator>(const State& other) const {
        return cost > other.cost;
    }
};

int main() {
    int N;
    cin >> N;
    
    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }
    
    vector<vector<int>> dist(N, vector<int>(N, INT_MAX));
    priority_queue<State, vector<State>, greater<State>> pq;
    
    dist[0][0] = grid[0][0];
    pq.push(State(0, 0, dist[0][0]));
    
    int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, 1, -1};
    
    while (!pq.empty()) {
        State current = pq.top();
        pq.pop();
        
        if (current.x == N-1 && current.y == N-1) {
            cout << current.cost << endl;
            return 0;
        }
        
        if (current.cost > dist[current.x][current.y]) continue;
        
        for (int i = 0; i < 4; i++) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];
            
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                int new_cost = current.cost + grid[nx][ny];
                if (new_cost < dist[nx][ny]) {
                    dist[nx][ny] = new_cost;
                    pq.push(State(nx, ny, new_cost));
                }
            }
        }
    }
    
    cout << dist[N-1][N-1] << endl;
    return 0;
}
