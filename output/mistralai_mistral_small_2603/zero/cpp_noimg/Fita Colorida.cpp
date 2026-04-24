
#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> fita(N);
    for (int i = 0; i < N; ++i) {
        cin >> fita[i];
    }

    queue<int> q;
    for (int i = 0; i < N; ++i) {
        if (fita[i] == 0) {
            q.push(i);
        }
    }

    vector<int> dist(N, INT_MAX);
    for (int i = 0; i < N; ++i) {
        if (fita[i] == 0) {
            dist[i] = 0;
        }
    }

    while (!q.empty()) {
        int pos = q.front();
        q.pop();
        int d = dist[pos];

        if (pos > 0 && dist[pos-1] > d + 1) {
            dist[pos-1] = d + 1;
            q.push(pos-1);
        }
        if (pos < N-1 && dist[pos+1] > d + 1) {
            dist[pos+1] = d + 1;
            q.push(pos+1);
        }
    }

    for (int i = 0; i < N; ++i) {
        if (fita[i] == -1) {
            if (dist[i] >= 9) {
                cout << 9;
            } else {
                cout << dist[i];
            }
        } else {
            cout << fita[i];
        }
        if (i < N-1) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}
