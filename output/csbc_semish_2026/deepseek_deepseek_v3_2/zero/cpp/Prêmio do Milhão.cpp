
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    long long soma = 0;
    int dias = 0;
    const long long META = 1000000;
    
    for (int i = 0; i < N; i++) {
        int A;
        cin >> A;
        soma += A;
        dias++;
        if (soma >= META) {
            cout << dias << endl;
            return 0;
        }
    }
    
    return 0;
}
