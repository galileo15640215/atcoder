#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using namespace std;

/*
int gcd(int a, int b)
{
    if (a < b) {
        a ^= b;
        b ^= a;
        a ^= b;
    }
    
    return b ? gcd(b, a % b) : a;
}
*/
int gcd(int a,int b)
{
	if (a%b==0)
	{
		return(b);
    }
	else
	{
		return(gcd(b,a%b));
    }
}

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int k, tmp;
    long long sum=0;
    cin>>k;
/*
    for(int i = 1; i < k+1; i++){
        for(int j = i; j < k+1; j++){
            for(int l = j; l < k+1; l++){
                tmp = __gcd(i, j);
                tmp = __gcd(tmp, l);           
                if(i == j && j == l){
                    sum += tmp;
                }
                else{
                    sum += tmp*3;
                }
            }
        }
    }
*/
    for(int i = 1; i < k+1; i++){
        for(int j = 1; j < k+1; j++){
            for(int l = 1; l < k+1; l++){
                tmp = __gcd(i, j);
                tmp = __gcd(tmp, l);           
                sum += tmp;
            }
        }
    }
    cout<<sum<<endl;
    return 0;
} 
