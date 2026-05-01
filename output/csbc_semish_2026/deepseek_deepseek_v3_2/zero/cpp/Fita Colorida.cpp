
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> fita(N);
    for (int i = 0; i < N; i++) {
        cin >> fita[i];
    }
    
    vector<int> dist(N, INT_MAX);
    
    int lastZero = -1;
    for (int i = 0; i < N; i++) {
        if (fita[i] == 0) {
            lastZero = i;
        }
        if (lastZero != -1) {
            dist[i] = min(dist[i], i - lastZero);
        }
    }
    
    lastZero = -1;
    for (int i = N - 1; i >= 0; i--) {
        if (fita[i] == 0) {
            lastZero = i;
        }
        if (lastZero != -1) {
            dist[i] = min(dist[i], lastZero - i);
        }
    }
    
    for (int i = 0; i < N; i++) {
        if (dist[i] > 9) {
            dist[i] = 9;
        }
        cout << dist[i];
        if (i < N - 1) {
            cout << " ";
        }
    }
    cout << endl;
    
    return 0;
}
