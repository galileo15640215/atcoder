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
    int n, s;
    vector<int> d;
    cin>>n;
    REP(i, n){
        cin>>s;
        d.push_back(s);
    }
    int ans = 0, arc, abc, abct = 0, cnt = 0;
    sort(ALL(d));
    for(int k = d[0]; k < d[n-1]+1; k++){
        abc = abct;
        for(int j = 0+cnt; j < d.size(); j++){
            if(k > d[j]){
                abc += 1;
                cnt += 1;
            }
            if(k <= d[j]){
                break;
            }
        }
        arc = d.size()-abc;
//        cout<<k<<" "<<arc<<" "<<abc<<endl;
        if(arc == abc){
            ans += 1;
        }
        if(arc < abc){
            break;
        }
        abct = abc;
    }
    cout<<ans<<endl;
    return 0;
}