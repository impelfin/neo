#include <stdio.h>

int x=5;

// 함수의 선언부
int add(int);

int main() {
	int y=3;
    	// 함수의 호출부
	printf("%d + %d = %d\n", x, y, add(y)); 
	return 0;
}

// 함수의 정의부
int add(int y) {
	return x + y;
}

