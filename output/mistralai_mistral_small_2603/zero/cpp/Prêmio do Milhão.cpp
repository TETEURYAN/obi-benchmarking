
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    long long total = 0;
    int dias = 0;
    for (int i = 0; i < N; i++) {
        int A;
        cin >> A;
        total += A;
        dias++;
        if (total >= 1000000) {
            break;
        }
    }
    cout << dias << endl;
    return 0;
}
