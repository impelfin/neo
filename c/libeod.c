#include <stdio.h>
#include "libcheckeod.h"

void main() {
        int n;
        while (1) {
        printf("Input number (0:Exit) : ");
        scanf("%d", &n);
        if(n == 0) {
            printf("Program Exit~!!\n\n");
            break;
        } else {
            if(checkeod(n) == 0) 
                printf("%d is even number~!!\n\n", n);
            else
                printf("%d is odd number~!!\n\n", n);
        }
    }
}
