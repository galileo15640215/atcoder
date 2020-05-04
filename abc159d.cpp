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
    int a[n];
    rep(i, n)
        cin>>a[i];
    int cnt, sum = 0;
    rep(i, n){
        for(int j = i+1; j < n; j++){
            if(a[i] == a[j]){
                sum += 1;
            }
        }
    }
    rep(i, n){
        cnt = 0;
        rep(j, n){
            if(i != j && a[i] == a[j]){
                cnt += 1;
            }
        }
        cout<<sum-cnt<<endl;
    }
    return 0;
}