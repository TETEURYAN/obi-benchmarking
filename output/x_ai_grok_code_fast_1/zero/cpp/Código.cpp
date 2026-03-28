
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    for(int &x : a) cin >> x;
    int count = 0;
    for(int i = 0; i <= N - 3; i++) {
        if(a[i] == 1 && a[i+1] == 0 && a[i+2] == 0) count++;
    }
    cout << count << endl;
    return 0;
}
