
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long A, B;
    Line(long long a, long long b) : A(a), B(b) {}
};

long long intersectionX(const Line& l1, const Line& l2) {
    return (l2.B - l1.B) / (l1.A - l2.A);
}

int main() {
    int N;
    long long X1, X2;
    cin >> N >> X1 >> X2;
    
    vector<Line> lines;
    for (int i = 0; i < N; ++i) {
        long long A, B;
        cin >> A >> B;
        lines.emplace_back(A, B);
    }
    
    int count = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            long long x = intersectionX(lines[i], lines[j]);
            if (x >= X1 && x <= X2) {
                count++;
            }
        }
    }
    
    cout << count << endl;
    return 0;
}
