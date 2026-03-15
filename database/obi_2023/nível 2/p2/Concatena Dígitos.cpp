#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, q;
  cin >> n >> q;
  vector<int> v(n + 1);
  vector<int> psum(n + 1, 0);
  for (int i = 1; i <= n; i++) {
    cin >> v[i];
    psum[i] = psum[i - 1] + v[i];
  }
  while (q--) {
    int l, r;
    cin >> l >> r;
    long long tam = r - l + 1;
    long long soma = psum[r] - psum[l - 1];
    long long resp = (tam - 1) * soma * 11;
    cout << resp << endl;
  }
  return 0;
}
