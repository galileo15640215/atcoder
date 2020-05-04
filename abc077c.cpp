#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using namespace std;
 
int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n;
    vector<int> a(n), b(n), c(n);
    cin>>n;
    rep(i, n)
        cin>>a[i];
    rep(i, n)
        cin>>b[i];
    rep(i, n)
        cin>>c[i];
    sort(all(a));
    sort(all(c));
    
    long long sum = 0;
    vector<int>::iterator iter_lower, iter_upper;
    long idx_lower, idx_upper;
    for (int i = 0; i < n; i++) {
        // lower_bound
        iter_lower = lower_bound(a.begin(), a.end(), b[i]);
        idx_lower = distance(a.begin(), iter_lower);
        // upper_bound
        iter_upper = upper_bound(c.begin(), c.end(), b[i]);
        idx_upper = distance(c.begin(), iter_upper);
        cout<<idx_lower<<" "<<idx_upper<<endl;
        cout<<*iter_lower<<" "<<*iter_upper<<endl;
        if(*iter_lower < b[i] && b[i] < *iter_upper){
            sum += (idx_lower+1)*(idx_upper+1);
        }
    }
    cout<<sum;
    return 0;
}