
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    long long soma = 0;
    int dias = 0;
    const long long meta = 1000000;
    
    for (int i = 0; i < N; i++) {
        long long A;
        cin >> A;
        soma += A;
        dias++;
        if (soma >= meta) {
            break;
        }
    }
    
    cout << dias << endl;
    return 0;
}
