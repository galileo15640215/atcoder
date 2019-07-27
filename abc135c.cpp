#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define ll long long
#define long long int
using namespace std;

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n, s;
    cin>>n;
    vector<int> a, b;
    rep(i, n+1){
        cin>>s;
        a.eb(s);
    }
    rep(i, n){
        cin>>s;
        b.eb(s);
    }
    int ans = 0;
    int next = 0;
    for(int i = 0; i < n+1; i++){
        if(i == n){
            ans += min(a[i], next);
        }
        else{
            ans += min(a[i], b[i]+next);
            if(b[i]+next < a[i]){
                next = 0;
                b[i] = 0;
            }
            else{
                a[i] -= next;
                if(a[i] <= 0){
                    a[i] == 0;
                }
                b[i] = b[i]-a[i];
                if(b[i] <= 0){
                    b[i] == 0;
                }        
                next = b[i];
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}