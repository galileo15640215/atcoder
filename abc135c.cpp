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
    int n, tmp;
    long long cnt = 0;
    cin>>n;
    int a[n+1], b[n];
    rep(i, n+1){
        cin>>a[i];
        cnt += a[i];
    }
    rep(i, n)
        cin>>b[i];

    if(a[0] <= b[0]){
        b[0] -= a[0];
        a[0] = 0;
    }
    else{
        a[0] -= b[0];
        b[0] = 0;
    }

    for(int i = 1; i < n; i++){
        if(a[i] <= b[i-1]){
            b[i-1] -= a[i];
            a[i] = 0;
        }
        else{
            a[i] -= b[i-1];
            b[i-1] = 0;
        }
        if(a[i] <= b[i]){
            b[i] -= a[i];
            a[i] = 0;
        }
        else{
            a[i] -= b[i];
            b[i] = 0;
        }
    }

    if(a[n] <= b[n-1]){
        b[n-1] -= a[n];
        a[n] = 0;
    }
    else{
        a[n] -= b[n-1];
        b[n-1] = 0;
    }
    long long ans = 0;
    rep(i, n+1)
        ans += a[i];
    cout<<cnt-ans<<endl;
    return 0;
}