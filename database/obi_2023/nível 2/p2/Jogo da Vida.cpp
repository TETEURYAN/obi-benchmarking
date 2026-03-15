#include <bits/stdc++.h>
using namespace std;

const int MAXN = 52;
const int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
const int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
char state[MAXN][MAXN], new_state[MAXN][MAXN];
int n;

bool in_bounds(int x, int y) {
  return x > 0 && x <= n && y > 0 && y <= n;
}

int count_alive_neighbors(int x, int y) {
  int alive = 0;
  for (int i = 0; i < 8; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (in_bounds(nx, ny) && state[nx][ny] == '1') alive++;
  }
  return alive;
}

void step() {
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      int alive_neighbors = count_alive_neighbors(i, j);
      new_state[i][j] = state[i][j];
      if (state[i][j] == '0' && alive_neighbors == 3) {
        new_state[i][j] = '1';
      }
      if (state[i][j] == '1' && (alive_neighbors < 2 || alive_neighbors > 3)) {
        new_state[i][j] = '0';
      }
    }
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      state[i][j] = new_state[i][j];
    }
  }
}

int main() {
  int q;
  cin >> n >> q;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      cin >> state[i][j];
    }
  }
  while (q--) {
    step();
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      cout << state[i][j];
    }
    cout << endl;
  }
  return 0;
}
