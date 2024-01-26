#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int busca_binaria(int lista [], int elemento, int inicio, int fim) {
    int meio = floor((inicio + fim) / 2);

    if ((inicio == fim) && (lista[meio] = elemento))
        return -1;
    else if (lista[meio] == elemento)
        return meio;
    else if (elemento < lista[meio])
        busca_binaria(lista, elemento, inicio, meio);
    else
        busca_binaria(lista, elemento, meio + 1, fim);
}


int main() {
    int v[10];
    int i;

    for (int i = 0; i < 10; i++) {
        v[i] = i;
    }
    int meio;
    meio = busca_binaria(v, 4, 1, 10);
    printf("\n");
    printf("%d", meio);
    system("PAUSE");
    return(0);
}
