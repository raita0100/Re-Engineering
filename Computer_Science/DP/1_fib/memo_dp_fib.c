#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 500

long int memo[MAX_SIZE] = {0};

long int mem_fib(int n){
  int f;
  if (memo[n] != 0){
    return memo[n];
  }
  else if(n < 2){
    f = 1;
  }
  else{
    f = mem_fib(n-1) + mem_fib(n-2);
  }
  memo[n] = f;
  return f;
}

int main(int argc, char *argv[]){
  int n = 0;
  long int res = 0;
  clock_t t;
  double t_took;

  if(argc > 1){
    n = atoi(argv[1]);
  }

  t = clock();
  res = mem_fib(n);
  t = clock() - t;

  printf("\n\tFIB : %ld\n", res);
  t_took = ((double)t)/CLOCKS_PER_SEC;
  printf("\n\tTime Elapsed : %f\n\n", t_took);
  return 0;
}
