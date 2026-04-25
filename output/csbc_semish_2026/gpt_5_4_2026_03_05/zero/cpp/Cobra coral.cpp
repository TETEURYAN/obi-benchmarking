#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a[4];
    for (int i = 0; i < 4; i++) cin >> a[i];

    bool verdadeira = false, falsa = false;

    for (int s = 0; s < 3; s++) {
        int t[4];
        for (int i = 0; i < 4; i++) t[i] = (s + i) % 3;
        if (a[0] == a[3] && a[0] != a[1] && a[0] != a[2] && a[1] != a[2]) {
            if (t[0] == t[3] && t[0] != t[1] && t[0] != t[2] && t[1] != t[2]) verdadeira = true;
        }
    }

    for (int s = 0; s < 3; s++) {
        int t[4];
        for (int i = 0; i < 4; i++) t[i] = (s + i) % 3;
        if (a[0] == a[3] && a[0] != a[1] && a[0] != a[2] && a[1] != a[2]) {
            if (t[0] == t[3] && t[0] != t[1] && t[0] != t[2] && t[1] != t[2]) falsa = true;
        }
    }

    int tv[4], tf[4];
    for (int i = 0; i < 4; i++) {
        tv[i] = (1 + i) % 3;
        tf[i] = i % 3;
    }

    auto comp = [&](int p[4]) {
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if ((a[i] == a[j]) != (p[i] == p[j]))
                    return false;
        return true;
    };

    if (comp(tv)) cout << "V\n";
    else cout << "F\n";

    return 0;
}