#include <stdio.h>
#include <conio.h>
#include <cstdlib>

/* Pointeiros s�o variaveis que apontam para endere�os
   de outras variaveis */

static int a = 0;


void  incrementar() {
	int b = 0;
	static int c = 0;
	
	printf("a: %d b: %d c: %d\n", a,b,c);
	
	a++;
	b++;
	c++;
	
	printf("a: %d b: %d c: %d\n", a,b,c);
	
}

int main() {
	int num = 10;
	int *ptr;
	ptr = &num;
	printf("Conteudo de num: %d \n", num);
	printf("Endere�o de num: %x \n", &num);
	printf("Conteudo de ptr: %x", ptr);
	printf("Acessando o conteudo de x pelo ponteiro: %d", *ptr);
	getch();
	return(0);
}
