#include <bits/stdc++.h>
using namespace std;
int main() {
    int N;
    cin >> N;
    long long sum = 0;
    int days = 0;
    for(int i = 0; i < N; i++) {
        long long A;
        cin >> A;
        sum += A;
        days++;
        if(sum >= 1000000) {
            cout << days << endl;
            return 0;
        }
    }
    return 0;
}