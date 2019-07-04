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
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }
const int MOD=1000000007;
 
int main(void){
  string s;
  cin>>s;
  int a=atoi(s.c_str());
  vector<int> l, ans;
  while(a>9){
	l.push_back(a%10);
    a /= 10;
  }
  reverse(ALL(l));
  
  REP(i, l.size()-2){
    int sum = l[i]*100+l[i+1]*10+l[i+2];
	ans.push_back(sum);
  }
  int m = abs(753-ans[0]);
  REP(i, ans.size()){
	if(abs(753-ans[i]) < m)
      m=abs(753-ans[i]);
  }
  cout<<m<<endl;
  return 0;
}