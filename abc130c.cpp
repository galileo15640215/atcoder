#include <bits/stdc++.h>
#define INF 1e9
#define ALL(v) v.begin(), v.end()
#define REP(i, n) for(int i = 0; i < n; i++)
#define max(v) *max_element(v.begin(), v.end())
#define min(v) *min_element(v.begin(), v.end())
using namespace std;
int is(int x, int y, int x1, int y1, int x2, int y2)
{
    int d;
    if (x1 > x2) {
        d = x1, x1 = x2, x2 = d;
        d = y1, y1 = y2, y2 = d;
    }
    return x1 <= x && x <= x2 &&
        ((y1 <= y2 && y1 <= y && y <= y2) ||
        (y1 > y2 && y2 <= y && y <= y1))
        && (y-y1)*(x2-x1) == (y2-y1)*(x-x1);
}
int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int w, h, x, y;
    cin>>w>>h>>x>>y;
    int ans = 0;
    if(x == w/2 and y == h/2)
        ans = 1;
    else if(is(x, y, 0, 0, w, h) or is(x, y, w, 0, 0, h))
       ans = 1;
    cout<<(double)((double)w*(double)h/2)<<" "<<ans<<endl;
    return 0;
}