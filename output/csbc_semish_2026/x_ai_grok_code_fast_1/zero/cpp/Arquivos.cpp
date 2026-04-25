
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    long long N, B;
    cin >> N >> B;
    vector<long long> files(N);
    for(auto &x : files) cin >> x;
    sort(files.begin(), files.end());
    long long left = 0, right = N-1;
    long long pastas = 0;
    while(left < right) {
        if(files[left] + files[right] <= B) {
            pastas++;
            left++;
            right--;
        } else {
            pastas++;
            right--;
        }
    }
    if(left == right) pastas++;
    cout << pastas << endl;
    return 0;
}
