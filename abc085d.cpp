#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int main(void){
    cin.tie(0);
    int n, h, p, q;
    cin>>n>>h;
    vector<int> a, b;
    for(int i = 0; i < n; i++){
        cin>>p>>q;
        a.push_back(p);
        b.push_back(q);
    }
    sort(b.begin(), b.end(), greater<int>());
    sort(a.begin(), a.end(), greater<int>());
    int m = a[0];
    int ans=0;
    while(h>0 && b.size() != 0){
      if(b[0]<m)
        break;
      h-=b[0];
      b.erase(b.begin());
      ans+=1;        
    }
    if(h>0)
  	  if(h%m == 0)
		ans+=h/m;
      else
        ans+=h/m+1;
//        ans+=ceil(h/m);
    cout<<ans<<endl;
    return 0;
}