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
    long long l, r;
    cin>>l>>r;

    /*
    for(int i = 1; i <= 2019; i++){
        for(int j = 1; j <= 2019; j++){
            l*
        }
    }
    */

    long long ans = 2019;
    if(r/2019 > l/2019){
        ans= 0;
    }else{
        for(long long i=l;i<r;i++){
            for(long long j=l+1;j<=r;j++){
                ans = min(ans,(i*j)%2019);
            }
        }
    }
    cout<<ans<<endl;

    return 0;
}