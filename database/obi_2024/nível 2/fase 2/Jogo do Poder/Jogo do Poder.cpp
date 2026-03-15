#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100010;
vector<long long int> poderes[MAXN], resp[MAXN];
vector<int> ativo[MAXN], indice[MAXN];
struct celula {
  int linha, coluna, poder;
};
bool cmp(celula a, celula b) {
  return a.poder < b.poder;
}
int pai[MAXN]; 
long long int soma[MAXN];
vector<celula> componente[MAXN];
int find(int v) {
  if(pai[v] == v) return v;
  return find(pai[v]);
}
void une(int a, int b) {
  a = find(a);
  b = find(b);
  
  if(a == b) return;
  
  if(componente[a].size() > componente[b].size()) swap(a, b);
  
  for(int i = 0; i < componente[a].size(); i++) {
    componente[b].push_back(componente[a][i]);
  }
  pai[a] = b;
  soma[b] += soma[a];
  componente[a].clear();
}
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int main() {
  int n, m; scanf("%d %d", &n, &m);
  vector<celula> celulas;
  int id = 0;
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++) {
      long long int p; scanf("%lld", &p);
      poderes[i].push_back(p);
      
      celula nova;
      nova.linha = i;
      nova.coluna = j;
      nova.poder = p;
      celulas.push_back(nova);
      
      id++;
      indice[i].push_back(id);
      ativo[i].push_back(0);
      
      resp[i].push_back(0);
    }
  sort(celulas.begin(), celulas.end(), cmp);
  
  for(int i = 0; i < celulas.size(); i++) {
    int l = celulas[i].linha;
    int c = celulas[i].coluna;
    int p = celulas[i].poder;
    
    ativo[l][c] = 1;
    int id = indice[l][c];
    componente[id].push_back(celulas[i]);
    pai[id] = id;
    soma[id] = p;
    for(int k = 0; k < 4; k++) {
      int vizl = l + dx[k];
      int vizc = c + dy[k];
      if(vizl < 0 || vizl >= n || vizc < 0 || vizc >= m) continue;
      if(ativo[vizl][vizc] == 0) continue;
      
      int vizid = indice[vizl][vizc];
      int vizpai = find(vizid);
      
      if(p <= soma[vizpai]) {
        une(id, vizpai);
      } else {
        for(int t = 0; t < componente[vizpai].size(); t++) {
          int lcel = componente[vizpai][t].linha;
          int ccel = componente[vizpai][t].coluna;
          resp[lcel][ccel] = soma[vizpai];
        }
        componente[vizpai].clear();
        une(vizpai, id);
      }
    }
  }
  
  int llast = (celulas.back()).linha;
  int clast = (celulas.back()).coluna;
  int idlast = indice[llast][clast];
  int pailast = find(idlast);
  for(int t = 0; t < componente[pailast].size(); t++) {
    int lcel = componente[pailast][t].linha;
    int ccel = componente[pailast][t].coluna;
    resp[lcel][ccel] = soma[pailast];
  }
  
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++)
      printf("%lld ", resp[i][j]);
    printf("\n");
  }
}