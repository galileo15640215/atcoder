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
    unsigned long long int a, b, c, q, sum, tmp;
    cin>>q;
    vector<unsigned long long int > x, d, n;
    REP(i, q){
        cin>>a>>b>>c;
        x.push_back(a);
        d.push_back(b);
        n.push_back(c);
    }
    REP(i, q){
        sum = x[i];
        for(unsigned long long int j=1; j < n[i]; j++){
            sum *= x[i]+j*d[i];
        }
        cout<<sum%1000003<<endl;
    }
    return 0;
}