#include <bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    // Verdadeira: BVBPBVBP -> pattern positions 0,1,2,3 = B,V,B,P
    // So a==c and b!=d and a!=b and a!=d and b!=c
    // Falsa: BVPBVPBV -> pattern positions 0,1,2,3 = B,V,P,B
    // So a==d and a!=b and a!=c and b!=c and b!=d and c!=d
    // Verdadeira pattern: x y x z where x!=y, x!=z, y!=z
    // Falsa pattern: x y z x where x!=y, x!=z, y!=z
    if(a==c && a!=b && a!=d && b!=d){
        cout<<"V"<<endl;
    } else {
        cout<<"F"<<endl;
    }
    return 0;
}