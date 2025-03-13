#include <stdio.h>

void main() {
    int x = 1;
    printf("Result : %d \n", *(char *)&x);

    if(*(char *)&x == 1)
        printf("This system is Little-Endian. \n");
    else 
        printf("This system is Big-Endian. \n");
}