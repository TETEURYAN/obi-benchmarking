
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,x1,y1,x2,y2;
    cin>>n>>x1>>y1>>x2>>y2;
    int half=n/2;
    // horizontal cut: one sticker in rows 1..half and other in rows half+1..n
    bool horiz=((x1<=half && x2>half)||(x2<=half && x1>half));
    // vertical cut: one sticker in cols 1..half and other in cols half+1..n
    bool vert=((y1<=half && y2>half)||(y2<=half && y1>half));
    if(horiz||vert) cout<<"S"<<endl;
    else cout<<"N"<<endl;
}
