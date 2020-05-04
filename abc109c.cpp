#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using namespace std;

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

    int n, y;
    cin>>n>>y;
    int x[n];
    rep(i, n)
        cin>>x[i];
    int tmp = abs(y-x[0]);
    rep(i, n){
        tmp = gcd(tmp, abs(y-x[i]));
    }
    cout<<tmp<<endl;
    return 0;
} 
