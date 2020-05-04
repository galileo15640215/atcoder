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

    int n, k;
    cin>>n>>k;
    double p[n], q[n], sum[n];
    rep(i, n){
        cin>>p[i];
        q[i] = (1+p[i])/2.0;
        if(i >= 1)
            sum[i] = sum[i-1] + q[i];
        else
            sum[i] = q[i];
    }
    double ma = -1;
    for(int i = k; i < n; i++){
        if(ma < sum[i] - sum[i-k])
            ma = sum[i] - sum[i-k];
    }
    /*
    rep(i, n)
        cout<<sum[i]<<" ";
    */
    cout<<fixed<<setprecision(6)<<ma<<endl;
    return 0;
}
