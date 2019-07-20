#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define ll long long
using namespace std;

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n, s;
    cin>>n;
    vector<int> a;
    rep(i, n){
        cin>>s;
        a.eb(s);
    }
    int ma;
    /*
    for(int i = 0; i < n; i++){
        ma = a[0];
        for(int j = 0; j < n; j++){
            if(i != j){
                if(ma < a[j]){
                    ma = a[j];
                }
            }
        }
        cout<<ma<<endl;
    }
    */
   /*
   int ma1, ma2;
   for(int i = 0; i < n; i++){
        if(i == 0){
            cout<<*max_element(a.begin()+1, a.end())<<endl;
        }
        else if(i == n-1){
            cout<<*max_element(a.begin(), a.end()-1)<<endl;
        }
        else{
            ma1 = *max_element(a.begin(), a.begin()+i-1);
            ma2 = *max_element(a.begin()+i+1, a.end());
            if(ma1 > ma2){
                cout<<ma1<<endl;
            }
            else{
                cout<<ma2<<endl;
            }
        }
   }
   */
    vector<int>t = a;
    sort(all(t));
    for(int i = 0; i < n; i++){
        if(a[i] == t[n-1]){
            cout<<t[n-2]<<endl;
        }
        else{
            cout<<t[n-1]<<endl;
        }
    }
    return 0;
}