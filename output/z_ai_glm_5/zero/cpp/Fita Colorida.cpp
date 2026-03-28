
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> fita(n);
    for (int i = 0; i < n; ++i) {
        cin >> fita[i];
    }

    // First pass: left to right
    // Initialize distance to a large value
    vector<int> dist(n, 100000); 

    for (int i = 0; i < n; ++i) {
        if (fita[i] == 0) {
            dist[i] = 0;
        } else {
            // If not the first element, check distance from the left
            if (i > 0) {
                dist[i] = dist[i-1] + 1;
            }
        }
    }

    // Second pass: right to left
    for (int i = n - 2; i >= 0; --i) {
        // Check distance from the right
        if (dist[i+1] + 1 < dist[i]) {
            dist[i] = dist[i+1] + 1;
        }
    }

    // Output the result
    for (int i = 0; i < n; ++i) {
        if (i > 0) cout << " ";
        // Cap the value at 9
        cout << min(dist[i], 9);
    }
    cout << endl;

    return 0;
}
