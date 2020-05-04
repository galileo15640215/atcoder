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

    char in[120];
    pair<pair<string,int>,int> p[110];
    int a;
    cin>>a;
    for(int i = 0; i < a; i++){
        int t;
        cin>>in>>t;
        string tmp = in;
        p[i] = make_pair(make_pair(in, -t), i);
    }
    sort(p, p+a);
    for(int i = 0; i < a; i++){
        cout<<p[i].second+1<<endl;
    }
    return 0;
}