#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100010;
const int MAXK = 18;
int pai[MAXN], ini[MAXN], fim[MAXN], prof[MAXN], dp[MAXN][MAXK];
vector<int> grafo[MAXN];
int tdfs;
int seg[4*MAXN];
void dfs(int v) {
  tdfs++;
  ini[v] = tdfs;
  for(int k = 1; k < MAXK; k++)
    dp[v][k] = dp[dp[v][k - 1]][k - 1];
  for(int i = 0; i < grafo[v].size(); i++) {
    int viz = grafo[v][i];
    dfs(viz);
  }
  fim[v] = tdfs;
}
int minProf(int a, int b) {
  if(prof[a] < prof[b]) return a;
  return b;
}
int query(int pos, int ini, int fim, int id) {
  if(id < ini || id > fim) return 0;
  if(ini == fim) return seg[pos];
  int m = (ini + fim)/2;
  int e = 2 * pos;
  int d = 2 * pos + 1;
  if(id <= m) return minProf(seg[pos], query(e, ini, m, id));
  return minProf(seg[pos], query(d, m + 1, fim, id));
}
void update(int pos, int ini, int fim, int p, int q, int v) {
  if(fim < p || ini > q) return;
  if(p <= ini && fim <= q) {
    seg[pos] = minProf(seg[pos], v);
    return;
  }
  int m = (ini + fim)/2;
  int e = 2 * pos;
  int d = (2 * pos) + 1;
  update(e, ini, m, p, q, v);
  update(d, m + 1, fim, p, q, v);
}
int pula(int v, int p) {
  for(int k = 0; k < MAXK; k++)
    if(p & (1<<k))
      v = dp[v][k];
  return v;
} 
int main() {
    int n; scanf("%d", &n);
    pai[1] = 1;
    dp[1][0] = pai[1];
    prof[1] = 0;
    prof[0] = n + 1;
    for(int i = 2; i <= n; i++) {
      scanf("%d", &pai[i]);
      dp[i][0] = pai[i];
      prof[i] = 1 + prof[pai[i]];
      grafo[pai[i]].push_back(i);
    }
    tdfs = 0;
    dfs(1);
    
    int q; scanf("%d", &q);
    for(int i = 1; i <= q; i++) {
      int t; scanf("%d", &t);
      if(t == 1) {
        int v, k; scanf("%d %d", &v, &k);
        int paiAtual = query(1, 1, tdfs, ini[v]);
        if(paiAtual == 0) paiAtual = pai[v];
        int resp = pula(paiAtual, k - 1);
        printf("%d\n", resp);
      } else {
        int v; scanf("%d", &v);
        if(ini[v] + 1 <= fim[v]) {
          update(1, 1, tdfs, ini[v] + 1, fim[v], v);
        }
      }
    }
}
