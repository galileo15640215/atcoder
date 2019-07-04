#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include<cstdio>
#include<iomanip>
#define INF 1e9
#define ALL(v) v.begin(), v.end()
#define REP(i, n) for(int i = 0; i < n; i++)
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
template<class T>bool chmax(T &former, const T &b) { if (former<b) { former=b; return true; } return false; }
template<class T>bool chmin(T &former, const T &b) { if (b<former) { former=b; return true; } return false; }
using namespace std;
 
int main(void){
  int n, k, toku;
  cin>>n>>k;
  double p, q, ans;
  int cnt;
  for(int i = 1; i <= n; ++i){
    toku=i;
    cnt = 0;
    while(toku<k){
      toku*=2;
      cnt+=1;
//      cout<<cnt<<endl;
    }
	p=(1/double(n))*pow(0.5, double(cnt));
//    cout<<p<<endl;
    ans+=p;
  }
  cout<<setprecision(12)<<ans<<endl;
  return 0;
}