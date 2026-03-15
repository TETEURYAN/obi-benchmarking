
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
        int j = i;
        while (j < N && a[j] == a[i]) {
            ++j;
        }
        ++phases;
        i = j;
    }

    std::cout << phases - 1 << std::endl;
    return 0;
}
