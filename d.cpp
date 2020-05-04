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

    int n, cnt = 0;
    string s;
    cin>>n>>s;
    int i = 0, k = n-1;
    bool flag = true;
    while (i < k) {
        for(int j = i+1; j < k; j++){
            if(j-i != k-j){
                if(s[i] != s[k] && s[i] != s[k] && s[j] != s[k]){
                    cnt += 1;
                }
            }            
        cout<<i<<" "<<j<<" "<<k<<endl;
        }
        /*
        if(flag){
            i += 1;
            flag = false;
        }
        else{
            k -= 1;
            flag = true;
        }
        */55
       i+=1;
    }
    cout<<cnt<<endl;
    return 0;
}
