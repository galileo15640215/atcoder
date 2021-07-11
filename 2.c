#include<stdio.h>
#include <string.h>

typedef struct string_pool{
    string_pool* next;
    string_pool* pre;
    char string[15];
    struct{};
}string_pool;


void re(char now[15],int p,int n,char s[15],string_pool* pool){
    if(p==n){
        string_pool now_pool;
        now_pool.pre=pool;
        now_pool.string=now;
        pool->next=&now_pool;

        return;
    }
    re(strcat(now,s[p]),p+1,n,s,pool);
    re(now,p+1,n,s,pool);
}

int main(void){
    char s[15];
    int N=0;
    int ans = 0;
    string_pool pool;
    pool.string="";

    /* 文字列の入力 */
    scanf("%s",s);
    /* 文字数のカウント */
    while(s[N]){
        N++;
    }

    re("",0,N,s,pool);
    printf("%s\n",str);
    printf("%d\n",str_l);
}
