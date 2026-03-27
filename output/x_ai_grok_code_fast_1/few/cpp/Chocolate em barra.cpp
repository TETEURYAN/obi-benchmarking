#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;
    int X1, Y1, X2, Y2;
    cin >> X1 >> Y1 >> X2 >> Y2;
    
    int mid = N / 2;
    
    bool vertical = (Y1 <= mid && Y2 > mid) || (Y1 > mid && Y2 <= mid);
    bool horizontal = (X1 <= mid && X2 > mid) || (X1 > mid && X2 <= mid);
    
    if (vertical || horizontal) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }
    
    return 0;
}