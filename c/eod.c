#include <stdio.h>

int eod(int x) {
	if (x % 2 == 0)
		printf("%d is even.\n", x);
	else   
		printf("%d is odd.\n", x);
}

void main() {
	int x;
	printf("Input number : ");
	scanf("%d", &x);
	eod(x);
}

