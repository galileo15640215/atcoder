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
 
    int n;
    cin>>n;
    int a[n];
    
    bool flag = true;
    rep(i, n){
        cin>>a[i];
    }
    sort(a, a+n);
    rep(i,n-1)
        if(a[i] == a[i+1])
            flag = false;

    if(flag){
        cout<<"YES"<<endl;
    }
    else{
        cout<<"NO"<<endl;
    }
    return 0;
}