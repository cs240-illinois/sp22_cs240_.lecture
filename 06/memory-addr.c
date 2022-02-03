#include <stdio.h>
#include <stdlib.h>

int main() {
  int val;
  printf("&val: %p\n", &val);

  int *ptr = malloc(sizeof(int));
  printf("&ptr: %p\n", &ptr);
  printf(" ptr: %p\n", ptr);

  int *ptr2 = malloc(sizeof(int));
  printf("&ptr2: %p\n", &ptr2);
  printf(" ptr2: %p\n", ptr2);

  return 0;
}