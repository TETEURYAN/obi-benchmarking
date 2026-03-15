
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long H, M, S, T;
    if (cin >> H >> M >> S >> T) {
        long long total_seconds = H * 3600 + M * 60 + S + T;
        
        long long new_S = total_seconds % 60;
        long long total_minutes = total_seconds / 60;
        long long new_M = total_minutes % 60;
        long long total_hours = total_minutes / 60;
        long long new_H = total_hours % 24;
        
        cout << new_H << "\n" << new_M << "\n" << new_S << "\n";
    }

    return 0;
}
