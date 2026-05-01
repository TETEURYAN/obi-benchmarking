#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    int count = 0;
    int state = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (state == 0 && x == 1) state = 1;
        else if (state == 1 && x == 0) state = 2;
        else if (state == 2 && x == 0) {
            count++;
            state = 0;
        }
        else if (state == 2 && x == 1) state = 1;
    }

    cout << count << endl;
    return 0;
}