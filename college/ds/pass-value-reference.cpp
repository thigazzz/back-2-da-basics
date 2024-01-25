#include <stdio.h>
#include <stdlib.h>

void troca_por_valor(int x, int y) {
    int aux;
    aux = x;
    x = y;
    y = aux;
}
void troca_por_referencia(int* x, int* y){
    int aux;
    if (x != NULL && y != NULL) {
        aux = *x;
        *x = *y;
        *y = aux;
    } 
}

int main() {
    int x, y;
    x = 10;
    y = 20;
    printf("valor de x: %d e valor de y é: %d", x, y);
    troca_por_valor(x, y);
    printf("valor de x: %d e valor de y é: %d", x, y);
    troca_por_referencia(&x, &y);
    printf("valor de x: %d e valor de y é: %d", x, y);
    return(0);
}
