#include <bits/stdc++.h>
using namespace std;
int main() {
  int n; scanf("%d", &n);
  int resp = 0;
  int first, last, maior;
  scanf("%d", &first);
  last = first;
  maior = first;
  for(int i = 2; i <= n; i++) {
    int cur; scanf("%d", &cur);
    maior = max(maior, cur);
    resp += abs(cur - last);
    
    last = cur;
  }
  resp += abs(maior - first);
  resp += abs(maior - last);
  printf("%d\n", resp/2);
}