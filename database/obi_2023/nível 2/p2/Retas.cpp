#include <bits/stdc++.h>
using namespace std;
#define int long long

bool cmp(pair<int,int> a, pair<int,int> b) {
	if(a.first != b.first) return a.first < b.first;
	return a.second > b.second;
}
long long ans = 0;
vector<int> mergesort(vector<int> v) {
	if(v.size() == 1) return v;

	vector<int> vl,vr;
    for(int i = 0; i < v.size()/2; i++) vl.push_back(v[i]);
    for(int i = v.size()/2; i < v.size(); i++) vr.push_back(v[i]);

	vl = mergesort(vl);
	vr = mergesort(vr);
	v.clear();
	int l = 0;
    int r = 0;

    while(l < vl.size() && r < vr.size()) {
        if(vl[l] < vr[r]) {
            // mover o l
            v.push_back(vl[l]);
            l++;
        }
        else {
            // mover o r
            v.push_back(vr[r]);
            r++;
            // aumentar as inversoes
            ans+= vl.size()-l;
        }
    }

    // coloca o que sobrou no final
    while(r < vr.size()) {
        v.push_back(vr[r]);
        r++;
    }
    while(l < vl.size()) {
        v.push_back(vl[l]);
        l++;
    }

    return v;
}

int32_t main() {
	int n, x1,x2;
	cin >> n >> x1 >> x2;
	vector<pair<int,int>> p;
	for(int i = 0; i < n; i++) {
		int a,b;
		cin >> a >> b;
		p.push_back(make_pair(a*x1+b,a*x2+b));
	}
	sort(p.begin(),p.end(),cmp);
	vector<int> v;
	for(auto x : p) v.push_back(x.second);

	mergesort(v);

	cout << ans << endl;
}
