#include <stdio.h>
#include <stdlib.h>

char _set[95] = {"\0"};

void init();

int main(int argc, char* argv[]){

  unsigned int max_mask_length;

  max_mask_length = ~0xabfcd289;//~(0x00000001 << 5);
  printf("\n\n%d\n\n", max_mask_length);
  //init();
  return 0;
}

void init(){

  int i, j;
  printf("\n[init] Initialising char set....\n");
  for (j=0, i = 32; i < 127; i+=1, j+=1){
    _set[j] = (char)i;
  }
  printf("\n[init] Initialization complete\n");

}
