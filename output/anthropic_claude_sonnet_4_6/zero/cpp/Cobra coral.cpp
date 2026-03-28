
#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    // Verdadeira: BVBPBVBP -> pattern of 4: pos0=B, pos1=V, pos2=B, pos3=P
    // So a==c and b!=d and a!=b and a!=d and b!=c... wait
    // Verdadeira pattern: B V B P -> a==c, b!=d, a!=b, a!=d, b!=c (b!=a already)
    // Falsa pattern: B V P B -> a==d, b!=c, a!=b, a!=c, b!=d... 
    // Let me think carefully
    // Verdadeira: BVBPBVBP... a 4-element window can be:
    // BVBP: [0]=B,[1]=V,[2]=B,[3]=P => pos0==pos2, pos1!=pos3, pos0!=pos1, pos0!=pos3, pos1!=pos2
    // VBPB: [0]=V,[1]=B,[2]=P,[3]=B => pos1==pos3, pos0!=pos2, pos0!=pos1, pos0!=pos3... 
    // BPBV: [0]=B,[1]=P,[2]=B,[3]=V => pos0==pos2
    // PBVB: [0]=P,[1]=B,[2]=V,[3]=B => pos1==pos3
    // So verdadeira: either pos0==pos2 or pos1==pos3 (one pair equal, the other not)
    // Falsa: BVPB: [0]=B,[1]=V,[2]=P,[3]=B => pos0==pos3
    // VPBV: pos0==pos3? no. [0]=V,[1]=P,[2]=B,[3]=V => pos0==pos3
    // PBVP: [0]=P,[1]=B,[2]=V,[3]=P => pos0==pos3
    // BVPB: pos0==pos3
    // So falsa: pos0==pos3 or pos1==pos2? 
    // VPBV: pos0==pos3 yes
    // PBVP: pos0==pos3 yes
    // BVPB: pos0==pos3 yes
    // What about starting at different offsets?
    // Falsa BVPBVP: windows are BVPB, VPBV, PBVP, BVPB -> all have pos0==pos3
    // Verdadeira BVBPBVBP: windows BVBP(0==2), VBPB(1==3), BPBV(0==2), PBVB(1==3)
    // So: if a==c || b==d => Verdadeira, if a==d || b==c => Falsa
    if(a==c || b==d) cout<<"V"<<endl;
    else cout<<"F"<<endl;
    return 0;
}
