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

    long long n, cnt = 0, r = 0, g = 0, b = 0;
    string s;
    cin>>n>>s;
    rep(i, n){
        if(s[i] == 'R') r++;
        else if(s[i] == 'G') g++;
        else b++;
    }
    rep(i, n){
        for(int j = i+1; j < n; j++){
            if(s[i] == s[j]) continue;
            int k = 2*j - i;
            if(s[k] == s[i] || s[k] == s[j] || k >= n) continue;
            cnt += 1;
        }
    }
    cout<<r*g*b-cnt<<endl;
    return 0;
}
