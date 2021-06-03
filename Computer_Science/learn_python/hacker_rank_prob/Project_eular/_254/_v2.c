#include <stdio.h>
#include <stdlib.h>

int FACTORIAL[10] = {0};
int *N;

void init(){

  int i;
  for (i = 0; i < 10; i+=1){
    if (i == 0)
      FACTORIAL[i] = 1;
    else
      FACTORIAL[i] = i * FACTORIAL[i-1];
  }
}

int get_sum(int n){
  int s = 0;
  while (n > 0){
    s += n%10;
    n = n%10;
  }
  return s;
}

int sf(int i){
  int ii = 1;
  
}

int main(void){

  return 0;
}
