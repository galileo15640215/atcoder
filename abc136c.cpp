#include <bits/stdc++.h>
#define INF 1e9
#define all(v) v.begin(), v.end()
#define rep(i, n) for(int i = 0; i < n; i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define ll long long
#define long long int
using namespace std;

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n, s;
    cin>>n;
    vector<int> h;
    rep(i, n){
        cin>>s;
        h.eb(s);
    }
    int key = 1;
    if(n==1){
        key == 1;   
    }
    else{
        /*
        for(int i=0 ; i<n-1; i++){
            if(h[i] - h[i+1] >= 2){
                cout<<"No"<<endl;
                key = 0;
                break;
            }
            else if(h[i] - h[i+1] == 1){
                h[i] = h[i]-1;
            }
        }
        for(int i=0 ; i<n-1; i++){
            if(h[i] - h[i+1] >= 1){
                cout<<"No"<<endl;
                key = 0;
                break;
            }
        }
        if(h[n-2] - h[n-1] >= 1 && key == 1){
            cout<<"No"<<endl;
            key = 0;
        }
        */
        for(int i=n-1 ; 0<i; i--){
            if(h[i-1] - h[i] >= 2){
                cout<<"No"<<endl;
                key = 0;
                break;
            }
            else if(h[i-1] - h[i] == 1){
                h[i-1] = h[i-1]-1;
            }
        }
        /*
        for(int i=n-1 ; 0<i; i--){
            if(h[i-1] - h[i] >= 1){
                cout<<"No"<<endl;
                key = 0;
                break;
            }
        }
        */
        if(h[0] - h[1] >= 1 && key == 1){
            cout<<"No"<<endl;
            key = 0;
        }
    }
    if(key==1){
        cout<<"Yes"<<endl;
    }
    return 0;
}