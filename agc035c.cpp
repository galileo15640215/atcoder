#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define ll long long
using namespace std;

// 数値を２進数文字列に変換
std::string to_binString(unsigned int val)
{
    if( !val )
        return std::string("0");
    std::string str;
    while( val != 0 ) {
        if( (val & 1) == 0 )  // val は偶数か？
            str.insert(str.begin(), '0');  //  偶数の場合
        else
            str.insert(str.begin(), '1');  //  奇数の場合
        val >>= 1;
    }
    return str;
}

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n, s;
    cin>>n;
    vector<int> a;
    vector<string> bit;
    rep(i,n){
        cin>>s;
        a.eb(s);
        bit.eb(to_binString(s));
    }
    a.eb(a[0]);
    bit.eb(bit[0]);
    int key = 1;
    /*
    for(int i = 1; i < n; i++){
        if(bit[i-1]^bit[i+1] == bitset<30>(pow(2, 30)){
            continue;
        }
        else{
            key == 0;
            break;
        }
    }
    if(key == 1){
        cout<<"Yes"<<endl;
    }
    else{
        cout<<"No"<<endl;
    }
    */
    return 0;
}