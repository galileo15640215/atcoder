#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using namespace std;

int gcd(long long a, long long b)
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

int lcm(long long a, long long b)
{
   return a * b / gcd(a, b);
}

int main(void){
    int n;
    cin>>n;
    long long ans = 1LL;
    rep(i, n){
        long long t;
        cin>>t;
        ans = lcm(ans, t);
    }
    cout<<ans<<endl;
    return 0;
} 
