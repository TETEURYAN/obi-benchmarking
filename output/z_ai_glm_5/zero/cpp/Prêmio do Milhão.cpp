
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    int total = 0;
    int days = 0;
    const int goal = 1000000;

    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        total += a;
        days++;
        if (total >= goal) {
            break;
        }
    }

    cout << days << endl;

    return 0;
}
