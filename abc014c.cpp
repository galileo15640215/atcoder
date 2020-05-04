#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using namespace std;
 
int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n;
    cin>>n;
    int a, b;
    int l[1000001];
    rep(i, n)
        l[i] = 0;
    rep(i, n){
        cin>>a>>b;
        l[a] += 1;
        l[b+1] -= 1;
    }
    int s[1000001];
    s[0] = l[0];
    for(int i=0;i<1000000;i++){
        s[i+1] = s[i] + l[i+1] ;
    }
    int m = 0;
    for(int i=0;i<1000001;i++){
        m = max(m,s[i]);
    }
    cout<<m<<endl;
    return 0;
} 
