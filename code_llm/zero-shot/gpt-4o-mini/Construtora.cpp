#include <iostream>
#include <vector>

int main() {
    int N;
    std::cin >> N;
    std::vector<int> a(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> a[i];
    }

    int phases = 0;
    for (int i = 0; i < N; ) {
        int height = a[i];
        while (i < N && a[i] == height) {
            ++i;
        }
        ++phases;
    }

    std::cout << phases << std::endl;
    return 0;
}