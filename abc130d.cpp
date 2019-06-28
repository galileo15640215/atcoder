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
    long long n, k;
    cin>>n>>k;
    long long  s;
    vector<long long> a;
    REP(i, n){
        cin>>s;
        a.emplace_back(s);
    }
    long long sum, ans = 0;
    for(long long i = 0; i < n; i++){
        sum = 0;
        for(long long j = i; j < n; j++){
            sum += a[j];
            if(sum >= k){
                ans += n-j;
                break;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}