#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main(){
  //找到 b在a里面第一次出现的位置
  char a[10] = "asbssssbs";
  char b[10] = "sbs";
  printf("%s\n", strstr(a,b));
  // cout << c << endl;
  // printf("%s\n", c);
  return 0;
}
