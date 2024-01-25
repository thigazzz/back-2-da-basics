/* Modulaização */
#include <stdio.h>
#include <stdlib.h>

int soma(int x, int y) {
	return x + y;
}

int main() {
	printf("A soma de 2 + 2 é: %d", soma(2,2));
	int x, *y, z;
	x = 5;
	y = &x;
	z = 10;
	scanf("%d", y);
	printf("%d %d", x, z);
	system("PAUSE");
	return(1);
}
