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
 
int main(void){
  int n, m, s, t;
  vector<int> a, b, c;
  cin>>n>>m;
  REP(i, n){
    cin>>s;
    a.push_back(s);
  }
  REP(i, m){
    cin>>s>>t;
    b.push_back(s);
    c.push_back(t);
  }
  REP(j, m){
    int cnt = b[j];
    REP(i, n){
      std::vector<int>::iterator iter= min_element(a.begin(), a.end());;
      size_t index = std::distance(a.begin(), iter);
      if(cnt == 0 || c[j]<=*iter)
        break;
      if(c[j]>*iter){
        a[index]= c[j];
        cnt--;
      }
    }
  }
  long sum=0;
  REP(i, n)
    sum+=(long)a[i];
  cout<<sum<<endl;
  return 0;
}