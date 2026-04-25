#include <bits/stdc++.h>

using namespace std;

const int MAX_VAL = 200005;

// Arrays to store the puzzle pieces information
// letter[id] stores the character of the piece with left number 'id'
// next_id[id] stores the right number of the piece with left number 'id'
char letter[MAX_VAL];
int next_id[MAX_VAL];

int main() {
    // Optimize I/O operations for performance
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    int e, d;
    char c;
    
    // Read N pieces
    for (int i = 0; i < n; i++) {
        cin >> e >> c >> d;
        letter[e] = c;
        next_id[e] = d;
    }

    // Start the traversal from the piece with left number 0
    int curr = 0;
    string result = "";
    
    // Traverse the chain N times
    // Since there is exactly one unique sequence, we can just iterate N times
    for (int i = 0; i < n; i++) {
        result += letter[curr];
        curr = next_id[curr];
    }

    cout << result << endl;

    return 0;
}