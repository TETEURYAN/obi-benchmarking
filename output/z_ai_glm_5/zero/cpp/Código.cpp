
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> seq(n);
    for (int i = 0; i < n; ++i) {
        cin >> seq[i];
    }

    int count = 0;
    for (int i = 0; i <= n - 3; ++i) {
        if (seq[i] == 1 && seq[i+1] == 0 && seq[i+2] == 0) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
