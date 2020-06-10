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
    int a, b, c, d, n;
    cin>>a>>b>>c>>d;
    cin>>n;
    string t;
    int l, sum = 0;
    rep(i, n){
      cin>>t>>l;
      int res = b;
      if(l > a){
          res += ceil(double(l-a)/double(c))*d;
      }
      if(t[0] == '0'){}
      else if(int(t[0])*10 + int(t[1]) >= 22){
          res *= 1.2;
      }
      sum += res;
    }
    cout<<sum<<endl;
    return 0;
}