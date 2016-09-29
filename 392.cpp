/*
* @Author: Lich_Amnesia
* @Date:   2016-09-29 10:13:15
* @Last Modified by:   Alwa
* @Last Modified time: 2016-09-29 10:13:18
*/

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int next[10000];
char s[10000];

void getnext(){
  int j = -1;
  next[0] = -1;
  for (int i = 1; i < strlen(s);i ++){
    while (j != -1 && s[j + 1] != s[i]) j = next[j];
    if (s[j + 1] == s[i]) j ++;
    next[i] = j;
  }
}
int main(){
  char t[11111];
  scanf("%s", t);
  scanf("%s", s);

  getnext();
  int j = -1;
  for (int i = 0; i < strlen(t); i ++){
    while (j != -1 && s[j + 1] != t[i]) {
      j = next[j];
    }
    if (s[j + 1] == t[i]) j ++;
    if (j == strlen(s) - 1){
      printf("%d\n", i - j);
      break;
    }
  }
  return 0;
}
