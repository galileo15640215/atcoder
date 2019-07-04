#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#define INF 1e9
#define ALL(v) v.begin(), v.end()
#define REP(i, n) for(int i = 0; i < n; i++)
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
template<class T>bool chmax(T &former, const T &b) { if (former<b) { former=b; return true; } return false; }
template<class T>bool chmin(T &former, const T &b) { if (b<former) { former=b; return true; } return false; }
using namespace std;
 
int gcd(int a, int b) {
  while(1) {
    if(a < b) swap(a, b);
    if(!b) break;
    a %= b;
  }
  return a;
}
int main(void){
  int n,t;
  vector<int> a;
  cin>>n;
  REP(i, n){
    cin>>t;
    a.push_back(t);
  }
  vector<int> left(n+1, 0), right(n+1, 0);
  REP(i, n)
    left[i+1] = gcd(left[i], a[i]);
  for(int i = n-1; i >= 0; --i){
    right[i] = gcd(right[i+1], a[i]);
  }
  int ans = 0;
  REP(i, n){
    int l = left[i];
    int r = right[i+1];
    chmax(ans, gcd(l, r));
  }
  cout<<ans<<endl;
  return 0;
}