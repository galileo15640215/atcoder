#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#define INF 1e9
#define ALL(v) v.begin(), v.end()
#define REP(i, n) for(int i = 0; i < n; i++)
using namespace std;
 
int main(void){
  int n, m;
  cin>>n>>m;
  vector<int> l, r;
  int s, t;
  REP(i, n){
    cin>>s>>t;
    l.push_back(s);
    r.push_back(t);
  }
  int maxl = 1;
  int minr = n;
  REP(i, n){
    maxl = max(maxl, l[i]);
    minr = min(minr, r[i]);
  }
  int ans = minr-maxl+1;
  ans = max(ans, 0);
  cout<<ans<<endl;
  return 0;
}
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#define INF 1e9
#define ALL(v) v.begin(), v.end()
#define REP(i, n) for(int i = 0; i < n; i++)
using namespace std;
 
int main(void){
  int n, m;
  cin>>n>>m;
  vector<int> l, r;
  int s, t;
  REP(i, n){
    cin>>s>>t;
    l.push_back(s);
    r.push_back(t);
  }
  int maxl = 1;
  int minr = n;
  REP(i, n){
    maxl = max(maxl, l[i]);
    minr = min(minr, r[i]);
  }
  int ans = minr-maxl+1;
  ans = max(ans, 0);
  cout<<ans<<endl;
  return 0;
}
提出情報