#include <bits/stdc++.h>
using namespace std;

int main() {
  int k, n;
  string alphabet, message;
  cin >> k >> n;
  cin >> alphabet;
  cin >> message;

  bool good_message = true;
  for (char c : message) {
    bool found_char = false;
    for (char d : alphabet) {
      if (c == d) found_char = true;
    }
    if (!found_char) good_message = false;
  }

  if (good_message) cout << "S" << endl;
  else cout << "N" << endl;
  return 0;
}
