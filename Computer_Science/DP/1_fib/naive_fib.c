#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int fib(int n){

	if (n < 2)
		return 1;

	return (fib(n-1) + fib(n-2));
}

int main(int argc, char *argv[]){
	clock_t t;
	int n=0;
	double t_took;
	/*
	printf("Enter a number : ");
	scanf("%d", &n);*/
	if (argc == 2){
		n = atoi(argv[1]);
	}
	t = clock();
	n = fib(n);
	t = clock()-t;
	printf("\n\nNumber : %d", n);
	t_took = ((double)t)/CLOCKS_PER_SEC;
	printf("\n\tTime taken : %f sec.\n\n", t_took);
	return 0;
}
