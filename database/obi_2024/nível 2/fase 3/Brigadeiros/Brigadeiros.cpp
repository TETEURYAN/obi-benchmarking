/*
OBI 2024 - Fase 3
  Brigadeiros
  Solução em O(9 * N^3)



  * Parte I: Algoritmo Guloso

  O primeiro passo deste problema é a seguinte observação gulosa:
  nunca é ótimo um membro do grupo fazer uma troca com um outro
  membro do grupo (pois essa troca não mudaria em nada as posições
  dos membros). Portanto, os membros do grupo se mantêm sempre na
  mesma ordem (entre eles) que estavam no início.

  Assim, se fixarmos quais pratos o grupo irá comer, sabemos
  exatamente qual membro irá comer cada prato:
    - o membro mais à esquerda comerá o prato escolhido mais à esquerda;
    - o segundo membro mais à esquerda comerá o segundo prato escolhido
      mais à esquerda;
    - e assim por diante.

  Essa observação nos permite resolver as subtarefas 2 e 3 com
  algoritmos de força bruta: basta enumerar todas as possibilidades
  de escolha de K pratos e testar, usando nosso algoritmo guloso,
  se é possível ou não alcançar os K pratos escolhidos em no máximo
  T segundos. Pegamos a maior soma entre as possibilidades válidas.
  
  Isto pode ser implementado:
    - com 3 loops encadeados em O(N^3) para a subtarefa 2 (13 pontos);
    - com bitmasks em O(2^N * K) para a subtarefa 3 (22 pontos);
    - com backtracking com podas em O(min(2^N, N^K) * K) para ambas
      as subtarefas 2 e 3 (35 pontos).



  * Parte II: Programação Dinâmica

  A outra ideia central para a resolução do problema é usar
  programação dinâmica (DP) para melhorar a complexidade das
  soluções força-bruta descritas acima.

  A DP mais natural de se construir é

    dp[a][b][t] := maior quantidade de brigadeiros que o prefixo
                   [1..b] dos membros do grupo consegue comer,
                   considerando apenas os pratos no prefixo [1..a],
                   gastando no máximo t segundos.

  Essa DP possui O(N^2 * T) estados. Podemos calcular a transição
  para o estado (a, b, t) em O(N) testando todas as opções possíveis
  para qual foi o índice do prato, abaixo representado por i,
  comido pelo último (b-ésimo) membro do grupo:

    dp[a][b][t] = max(dp[i - 1][b - 1][t - dist(i, b)] + p[i])
                  para i <= a e dist(i, b) <= t

    onde dist(i, b) representa a distância entre a posição i e
    a posição do b-ésimo membro do grupo.

  Esta solução tem complexidade total O(N^3 * T) e é suficiente
  para as subtarefas 2, 3 e 4 (58 pontos).


  Para as subtarefas finais, três otimizações são necessárias:

    #1: Perceba que N^2 é tempo suficiente para alcançar qualquer
        conjunto de K pratos, então podemos redefinir
          T = min(T, N^2)
        e obter uma DP com N^4 estados.

    #2: Podemos otimizar a transição da DP acima para O(1):
        escolhemos entre parear ou não parear o a-ésimo prato
        com o b-ésimo membro do grupo:

        dp[a][b][t] = max(
                        dp[a - 1][b - 1][t - dist(a, b)] + p[a],
                        dp[a - 1][b][t]
                      )
        onde o primeiro caso só vale se t >= dist(a, b).

    #3: A resposta (total de brigadeiros comidos) é razoavelmente
        pequena: no máximo 9N. Assim, podemos "inverter" a DP e
        definir a seguinte DP com 9 * N^3 estados:

        dp_inv[a][b][c] := menor tempo necessário para comer c
                           brigadeiros, considerando apenas o
                           prefixo [1..a] dos pratos e [1..b]
                           dos membros do grupo.

        A transição pode ser feita com ou sem a otimização #2,
        em O(N) ou O(1) respectivamente.
        A versão mais rápida, em O(1), fica

        dp_inv[a][b][c] = min(
                          dp_inv[a - 1][b - 1][c - p[a]] + dist(a, b),
                          dp_inv[a - 1][b][c],
                        )

        A resposta é o maior C tal que dp_inv[N][K][C] <= T.

        Os casos base e outros detalhes ficam como exercício ao leitor.

  A pontuação de acordo com as otimizações feitas fica assim:
    - Otimização #1: resolve até subtarefa 5 (68 pontos)
    - Otimização #2: resolve até subtarefa 5 (68 pontos)
    - Otimizações #1 e #2: resolve até subtarefa 6 (79 pontos)
    - Otimização #3: resolve até subtarefa 6 (79 pontos)
    - Otimizações #2 e #3: resolve todas as subtarefas (100 pontos)

  O código abaixo implementa a solução para 100 pontos com
  otimização de memória (não era necessário para 100 pontos,
  mas é mais eficiente na prática).
*/

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 301;
const int INF = 1e9 + 10;
const int MAXC = 9 * MAXN;

// aqui usamos otimização de memória,
// então estamos calculando dp_inv[a % 2][b][c]
// da solução acima
int dp[2][MAXN][MAXC];

int qtd[MAXN];
bool amigo[MAXN];
vector <int> grupo;
int n, k;
int t;

int main() {
  int x;
  cin >> n >> k >> t;
  for (int i = 1; i <= n; i++) {
    cin >> qtd[i];
  }
  for (int i = 1; i <= n; i++) {
    cin >> x;
    if (x == 1) {
      amigo[i] = true;
      grupo.push_back(i);
    }
  }

  for (int i = 0; i < 2; i++) {
    for (int b = 0; b <= k; b++) {
      for (int c = 0; c < MAXC; c++) {
        if ((i == 0 || b == 0) && c == 0) {
          dp[i][b][c] = 0;
        }
        else {
          dp[i][b][c] = INF;
        }
      }
    }
  }

  for (int a = 1; a <= n; a++) {
    int i = a % 2;
    for (int b = 1; b <= k; b++) {
      for (int c = 0; c < MAXC; c++) {
        if (qtd[a] <= c) {
          dp[i][b][c] = min(
            dp[i][b][c],
            dp[1 - i][b - 1][c - qtd[a]] + abs(a - grupo[b - 1]));
        }
        dp[i][b][c] = min(dp[i][b][c], dp[1 - i][b][c]);
      }
    }
  }

  for (int l = MAXC - 1; l >= 0; l--) {
    if (dp[n % 2][k][l] <= t) {
      cout << l << endl;
      return 0;
    }
  }
}
