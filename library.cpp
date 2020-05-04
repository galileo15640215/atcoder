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

int lcm(int a, int b)
{
   return a * b / gcd(a, b);
}

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);

    sort(a, a+n);
    // first, last はソートした配列のイテレータ
    // key は検索したい数値
    std::binary_search(first, last, key)
    std::lower_bound(first, last, key)
    std::upper_bound(first, last, key)
    return 0;
}

    vector<int> vec = {1, 1, 2, 2, 4, 5, 5, 6, 8, 8, 8, 10, 15};
    vector<int>::iterator iter_lower, iter_upper;
    long idx_lower, idx_upper;
    for (int key = 0; key <= 16; ++key) {
        // lower_bound
        iter_lower = lower_bound(vec.begin(), vec.end(), key);
        idx_lower = distance(vec.begin(), iter_lower);

        // upper_bound
        iter_upper = upper_bound(vec.begin(), vec.end(), key);
        idx_upper = distance(vec.begin(), iter_upper);

        // output
        cout << "----- key = " << key << " -----" << "\n";
        cout << "lower_bound: vec[" << idx_lower << "] = " << *iter_lower << "\n";
        cout << "upper_bound: vec[" << idx_upper << "] = " << *iter_upper << "\n";
        cout << "\n";
//累積和
//小数桁固定
    cout<<fixed<<setprecision(6)<<sum<<endl;