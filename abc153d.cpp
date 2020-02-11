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

    long long h, cnt = 0, mon = 1, ans = 0;
    cin>>h;
    while(h > 0){
        if(h > 1){
            ans += mon;
            h /= 2;
            mon *= 2;
        }
        else{
            ans += mon;
            break;
        }
    }
    cout<<ans<<endl;
    return 0;
}