
#include <iostream>

int main() {
    int N;
    std::cin >> N;
    long long soma = 0;
    int dias = 0;
    for (int i = 0; i < N; ++i) {
        int A;
        std::cin >> A;
        soma += A;
        dias++;
        if (soma >= 1000000) {
            break;
        }
    }
    std::cout << dias << std::endl;
    return 0;
}
