#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> v(n);
  for (int &x : v) cin >> x;
  sort(v.begin(), v.end());
  cout << v[n - k] << endl;
  return 0;
}
