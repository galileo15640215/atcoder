#include <iostream>
#include <algorithm>
 
using namespace std;
 
int main(void){
    int a, b, c, d;
    cin >> a >> b;
    c = max(a, b);
    d = min(a, b);
    if(c <= 8 && d <= 8)
        cout<< "Yay!" << "\n";
    else if(c >= 9 || d >= 9)
        cout<< ":(" << "\n";
    return 0;
}