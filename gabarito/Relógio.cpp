#include <bits/stdc++.h>
using namespace std;

int main() {
  int hrs, minu, secs, t;
  cin >> hrs >> minu >> secs >> t;

  secs += t;
  minu += (secs / 60);
  secs %= 60;
  hrs += (minu / 60);
  minu %= 60;
  hrs %= 24;
  
  cout << hrs << endl;
  cout << minu << endl;
  cout << secs << endl;
  return 0;
}