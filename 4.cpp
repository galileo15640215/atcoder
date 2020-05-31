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
    int a[n], b[n];
    vector<float> ans;
    rep(i, n){
        cin>>a[i]>>b[i];
        tmp = b[i]-a[i];
        rep(j, ans.size()){
            if(tmp == ans[j]){
                flag = false;
                break;
            }
            if(flag){
                ans.pb(tmp);
            }
        }
    }
    cout<<ans.size()<<endl;
    return 0;
}