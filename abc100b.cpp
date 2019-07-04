#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
 
using namespace std;
 
int main(void){
    int d, n, ans, cnt = 0;
    vector<int> l(100);
    cin >>d>>n;
    for(int i = 1; i < 100000000; i++){
        if(i%int(pow(100, d)+1) == 0){
            l[cnt] = i;
            cnt += 1;
        }
        if(cnt == n)
            break;
    }
    cout<<l[n-1]<<"\n";
    return 0;
}