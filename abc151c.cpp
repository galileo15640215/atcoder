#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
#define PI 3.141592653589793
using namespace std;
 
int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);

    int N, M;
    int WA[105000];
    bool AC[105000];
    cin >> N >> M;
    int WAnum = 0;
    int ACnum = 0;
    for(int i = 1; i <= N; i++) {
        WA[i] = 0;
        AC[i] = false;
    }
    while(M--) {
        int p;
        string S;
        cin >> p >> S;
        if(AC[p]) continue;
        if(S == "AC") {
            AC[p] = true;
            ACnum++;
            WAnum += WA[p];
        } else if(S == "WA") {
            WA[p]++;
        }
    }

    cout << ACnum << " " << WAnum << endl;
    return 0;
}