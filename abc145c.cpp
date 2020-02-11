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
    int n;
    cin>>n;
    vector<long double> x(n), y(n);
    rep(i, n)
        cin>>x[i]>>y[i];
    long double ans = 0;
    long double sum = 0;
    vector<int> v;
    rep(i, n)
        v.pb(i);
    do {
        sum = 0;
        rep(i, n-1)
            sum += sqrt((x[v[i]]-x[v[i+1]])*(x[v[i]]-x[v[i+1]]) + (y[v[i]]-y[v[i+1]])*(y[v[i]]-y[v[i+1]]));
        ans += sum;
    } while( next_permutation(v.begin(), v.end()) );     // 次の順列を生成
    int fac = 1;
    for(int i = 2; i < n+1; i++){
        fac *= i;
    }
    cout << fixed << setprecision(10) << ans / fac << endl;
    return 0;
}