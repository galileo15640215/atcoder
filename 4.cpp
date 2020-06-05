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
    int n, x, cnt = 0;
    cin>>n>>x;
    int a[n];
    rep(i, n)
        cin>>a[i];
    rep(i, n-1){
        for(int j = i+1; j < n; j++){
            if(a[i]^a[j] == x){
                cout<<a[i]^a[j]<<endl;
                cnt += 1;
            }
        }
    }
    cout<<cnt<<endl;
    return 0;
}