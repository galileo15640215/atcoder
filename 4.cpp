#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using namespace std;

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n;
    cin>>n;
    vector<string> s;
    rep(i, 5){
        string ms;
        cin>>ms;
        s.pb(ms);
    }
    vector<string> nums;
    /*string num = ".###..#..###.###.#.#.###.###.###.###.###..#.#.##....#...#.#.#.#...#.....#.#.#.#.#..#.#..#..###.###.###.###.###...#.###.###..#.#..#..#.....#...#...#.#.#...#.#.#...#..###.###.###.###...#.###.###...#.###.###.";
    */
    string num1 = ".###..#..###.###.#.#.###.###.###.###.###.";
    string num2 = ".#.#.##....#...#.#.#.#...#.....#.#.#.#.#.";
    string num3 = ".#.#..#..###.###.###.###.###...#.###.###.";
    string num4 = ".#.#..#..#.....#...#...#.#.#...#.#.#...#.";
    string num5 = ".###.###.###.###...#.###.###...#.###.###.";

    for(int k = 0; k < 10; k++){
        string n0 = "";
        for(int i = 0; i < 4; i++){
            n0 += num1[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += num2[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += num3[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += num4[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += num5[k*4+i];
        }
        nums.pb(n0);
    }

    vector<string> snums;
    string snum1 = s[0];
    string snum2 = s[1];
    string snum3 = s[2];
    string snum4 = s[3];
    string snum5 = s[4];

    for(int k = 0; k < n; k++){
        string n0 = "";
        for(int i = 0; i < 4; i++){
            n0 += snum1[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += snum2[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += snum3[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += snum4[k*4+i];
        }
        for(int i = 0; i < 4; i++){
            n0 += snum5[k*4+i];
        }
        snums.pb(n0);
    }

    /*
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 5; j++){
            for(int k = 0; k < 4; k++){
                cout<<nums[i][j*4+k];
            }
            cout<<endl;
        }
    }
    */
    string ans = "";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < 10; j++){
            bool flag = true;
            if(snums[i] != nums[j]){
                flag = false;
            }
            if(flag){
                ans += to_string(j);
            }
        }        
    }
    cout<<ans<<endl;
    return 0;
}