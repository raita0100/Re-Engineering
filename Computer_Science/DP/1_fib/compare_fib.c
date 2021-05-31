#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 500

long int memo[MAX_SIZE] = {0};

long int mem_fib(int n){
  long int f;
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

long int rec_fib(long int n){

	if (n < 2)
		return 1;

	return (rec_fib(n-1) + rec_fib(n-2));
}

long int naive_fib(int n){
  int i;
  long int  a = 1, b = 1;
  for (i = 2; i <= n; i+=1){
    a = a + b;
    b = a - b;
  }
  return a;
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
  res = naive_fib(n);
  t = clock() - t;

  printf("\n\tFIB(%d) by naive_fib : %ld\n", n, res);
  t_took = ((double)t)/CLOCKS_PER_SEC;
  printf("\n\tTime Elapsed by naive_fib: %f\n\n", t_took);

  t = clock();
  res = mem_fib(n);
  t = clock() - t;

  printf("\n\tFIB(%d) by mem_fib : %ld\n", n, res);
  t_took = ((double)t)/CLOCKS_PER_SEC;
  printf("\n\tTime Elapsed by mem_fib: %f\n\n", t_took);

  if (n < 43){

    t = clock();
    res = rec_fib(n);
    t = clock() - t;

    printf("\n\tFIB(%d) by rec_fib : %ld\n", n, res);
    t_took = ((double)t)/CLOCKS_PER_SEC;
    printf("\n\tTime Elapsed by rec_fib: %f\n\n", t_took);
  }
  else{
    printf("\nFIB(%d) by rec_fib will be so branching lor number > 42......\n\n", n);
  }


  return 0;
}
