#include<bits/stdc++.h>
#define all(x) begin(x), end(x)
#define ff first
#define ss second
#define O_O
using namespace std;
template <typename T>
using bstring = basic_string<T>;
template <typename T>
using matrix = vector<vector<T>>;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef double dbl;
typedef long double dbll; 
const ll INFL = 4e18+25;
const int INF = 1e9+42;
const double EPS = 1e-7;
const int MOD = 1e9+7;
const int RANDOM = chrono::high_resolution_clock::now().time_since_epoch().count();
const int MAXN = 1e6+1;

struct effect{
    ll a, b;


    effect operator*(effect o){
        return {(a*o.a)%MOD, (b*o.a+o.b)%MOD};
    }

    ll apply(ll x) const{
        return a*x+b;
    }
    bool operator<(effect o) const{
        return o.apply(apply(1)) > apply(o.apply(1));
    }

    effect operator-(effect x){
        return {a-x.a, b-x.b};
    }

    ll cross(effect x){
        return a*x.b-b*x.a;
    }
};

effect power(effect in, int exp){
    effect ret = {1,0};
    while(exp){
        if(exp&1){
            ret = ret*in;
        }
        in = in*in;
        exp>>=1;
    }
    return ret;
}


int main(){
    
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m, k;
    cin >> n >> m >> k;

    vector<effect> feit(n), esp(m);


    for(auto& i : feit)
        cin >> i.a;
    for(auto& i : feit)
        cin >> i.b;

    sort(all(feit), [&](effect a, effect b){
        return make_pair(a.a,a.b) < make_pair(b.a, b.b);
    });

    vector<effect> hull;

    auto check =[&] (effect eff) -> bool {
        int k = hull.size();

        return (eff-hull[k-2]).cross(hull[k-1]-hull[k-2]) <= 0;
    };

    for(auto [a,b] : feit){
        while(hull.size() >= 2 && check({a,b})){
            hull.pop_back();
        }
        hull.push_back({a,b});
    }

    feit = hull;
    n = feit.size();

    // cerr << "hull: " << n << '\n';

    for(auto& i : esp)
        cin >> i.a;
    for(auto& i : esp)
        cin >> i.b;

    sort(all(esp));

    effect resp2 = {1,0};

    for(auto i : esp){
        resp2 = resp2*i;
    }
    
    effect best = {0,0};

    for(int i = 0; i < n; i++){
        if(feit[i].a > best.a){
            best = feit[i];
        }
        if(feit[i].a >= best.a && feit[i].b >= best.b)
            best = feit[i]; 
    }

    int q;
    cin >> q;

    while(q--){
        ll x;
        cin >> x;

        ll resp1 = x;
        bool bigyoshi = 0;

        if(best.a == 1){
            (resp1 = x+ll(k)*best.b)%=MOD;
        } else for(int i = 0; i < k; i++){
            if(bigyoshi){
                resp1 = power(best, k-i).apply(resp1)%MOD;
                break;
            } else {
                int ini = 0, fim = n-1;

                while(ini != fim){
                    int m = (ini+fim)>>1;
                    if(feit[m].apply(resp1) >= feit[m+1].apply(resp1)){
                        fim = m;
                    } else ini = m+1;
                }

                // for(int i = 0; i < n; i++)
                //     cerr << feit[i].apply(resp1) << ' ';
                // cerr << '\n';
                // cerr << complex{feit[ini].a, feit[ini].b} << '\n';
                
                resp1 = feit[ini].apply(resp1);
                if(resp1 >= MOD)
                    resp1 %= MOD, bigyoshi = 1;
            }
        }

        cout << resp2.apply(resp1)%MOD << '\n';
    }
    
    return 0;

}
