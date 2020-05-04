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

    long long h, w;
    cin>>h>>w;
    if(h == 1 || w == 1){
        cout<<1<<endl;
    }
    else{
        if(h*w%2 == 0){
            cout<<h*w/2<<endl;
        }
        else{
            cout<<h*w/2+1<<endl;
        }
    }
    return 0;
}