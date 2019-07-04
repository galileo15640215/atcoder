#include <bits/stdc++.h>
#define INF 1e9
#define ALL(v) v.begin(), v.end()
#define REP(i, n) for(int i = 0; i < n; i++)
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
using namespace std;
 
int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n, m;
    cin>>n>>m;
    int s;
    int a[m];
    REP(i,m){
        cin>>s;
        a[i] = s;
    }
    unsigned long long dp[100100] = {0};
    int key,tmp = 0;
    dp[0] = 1;
    for(int i = 1; i < n+1; i++){
        if(i == 1 and a[0] != 1){
            dp[1] += 1;
        }
        else{
            key = 0;
            for(int j = tmp; j < m; j++){
                if(i == a[j]){
                    key = 1;
                    tmp = j;
                    break;
                }
            }
            if(key == 0){
                dp[i] += dp[i-1];
                dp[i] += dp[i-2];
                dp[i] %= 1000000007;
            }
        }
    }
    /*
    REP(i, n+1){
        cout<<i<<dp[i]<<endl;
    }
    */
    cout<<dp[n]%1000000007<<endl;
    return 0;
}