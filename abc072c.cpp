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
  int n, t;
  vector<int> v, b(1000000);
  cin>>n;
  REP(i, n){ cin>>t; v.push_back(t);}
  REP(i, n){
	REP(j, max(v)+2){
	  if(v[i]==j && v[i]!=0){
        b[j]+=1;
        b[j-1]+=1;
        b[j+1]+=1;
	  }
      else if(v[i]==j && v[i] == 0){
        b[j]+=1;
        b[j+1]+=1;
      }
    }
  }
//  REP(i, max(v)+2)cout<<i<<b[i]<<endl;
  cout<<max(b)<<endl;
  return 0;
}