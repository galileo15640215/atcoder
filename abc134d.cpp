#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define ll long long
using namespace std;

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n, s, sum = 0;
    cin>>n;
    vector a, b;
    rep(i, n){
        cin>>s;
        a.eb(s);
        sum += s;
    }
    for(int i = 1; i < n+1; i++){
        if(a[0] == 1 && i == 1){
            if(sum%2 == 1){
                b.pb(1);
            }
        }
        if(a[i] == 1){
            int sum1;
            for(int j == i; j < n+1; j+=i){
                sum1 += a[j];
            }
            if(sum1%2 == 1){
                b.pb(sum1%2);
            }
        }
    }
    return 0;
}