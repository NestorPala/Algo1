#include <stdio.h>
#define len(x) (sizeof(x) / sizeof(x[0]))


void ordenar_arreglo(int lista[], int len) {
    int aux = 0;

    for (int i=0; i<len; i++) {
        for (int j=0; j<len-i-1; j++) {
            if (lista[j] > lista[j + 1]) {
                aux = lista[j];
                lista[j] = lista[j + 1];
                lista[j + 1] = aux;
            }
        }
    }
}


int main() {
    int lista[] = {12, 35, 4, 23, 8, -124, 985, 1000, -12, 3, 345, -121, 98};

    printf("Largo de la lista: %d elementos\n", len(lista));
    ordenar_arreglo(lista, len(lista));

    for (int i=0; i<len(lista); i++) {
        printf("%d  ", lista[i]);
    }

    return 0;
}
