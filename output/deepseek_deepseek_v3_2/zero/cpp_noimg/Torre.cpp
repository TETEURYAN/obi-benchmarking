
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    
    vector<vector<int>> grid(N, vector<int>(N));
    vector<int> rowSum(N, 0);
    vector<int> colSum(N, 0);
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
            rowSum[i] += grid[i][j];
            colSum[j] += grid[i][j];
        }
    }
    
    int maxWeight = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int weight = rowSum[i] + colSum[j] - 2 * grid[i][j];
            if (weight > maxWeight) {
                maxWeight = weight;
            }
        }
    }
    
    cout << maxWeight << '\n';
    
    return 0;
}
