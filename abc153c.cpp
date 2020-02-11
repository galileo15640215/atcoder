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

    int n, k, t;
    cin>>n>>k;
    vector<int> h;
    rep(i, n){
        cin>>t;
        h.pb(t);
    }
    sort(all(h));
    for(int i = 0; i < k; i++){
        if(i > n){
            break;
        }
        h[n-1-i] = 0;
    }
    long long sum = 0;
    rep(i, n){
        sum += h[i];
    }
    cout<<sum<<endl;
    return 0;
}