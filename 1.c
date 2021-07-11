#include<stdio.h>
#include <string.h>

typedef struct string_pool_t{
    struct string_pool_t* next;
    struct string_pool_t* pre;
    char* string;
}string_pool_t;


void re(char now[15],int p,int n,char s[15],string_pool_t* pool){
    if(p==n){
        string_pool_t now_pool;
        now_pool.pre=pool;
        now_pool.string=now;
        pool->next=&now_pool;

        return;
    }

    re(now,p+1,n,s,pool);
    strcat(now,&s[p]);
    re(now,p+1,n,s,pool);
}

int main(void){
    char s[15];
    int N=0;
    int ans = 0;
    string_pool_t pool;
    char* tmp="";

    /* 文字列の入力 */
    scanf("%s",s);
    /* 文字数のカウント */
    while(s[N]){
        N++;
    }
    pool.string=tmp;

    re("",0,N,s,&pool);
}