#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

void re(string now,int p,int n,string s,map<string,int>&A){
    if(p==n) {
        if(now!="")A[now]=1; //空文字でなければ追加
        return;
    }
    re(now+s[p],p+1,n,s,A); // p番目を追加する
    re(now,p+1,n,s,A); //p番目を追加しない
}

int main(){
    int ans= 0;
    string s; // 文字列入力
    cin >> s;
    int n=s.size(); // 文字サイズn 
    map<string,int> A; 
    re("",0, n,s,A);

    cout<<A.size()<<endl; // 保存した文字列のサイズが答え
}