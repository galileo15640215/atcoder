#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rall(v) v.begin(), v.end(), std::greater<int>()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
using namespace std;

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n, k, q, t;
    cin>>n>>k>>q;
    int p[n];
    rep(i, n){
        p[i] = k-q;
    }
    rep(i, q){
        cin>>t;
        p[t-1] += 1;
    }
    
    rep(i, n)
        if(p[i] <= 0)
            cout<<"No"<<endl;
        else
            cout<<"Yes"<<endl;

    return 0;
}