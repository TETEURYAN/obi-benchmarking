#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  int resp[4];
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      for (int k = 1; k <= n; k++) {
        int bordas = 0;
        if (i == 1 || i == n) bordas++;
        if (j == 1 || j == n) bordas++;
        if (k == 1 || k == n) bordas++;
        resp[bordas]++;
      }
    }
  }
  for (int i = 0; i < 4; i++) {
    cout << resp[i] << endl;
  }
  return 0;
}
