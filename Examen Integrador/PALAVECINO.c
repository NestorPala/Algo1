//INTEGRADOR DE ALGORITMOS Y PROGRAMACIÓN I
//2021-08-17
//PALAVECINO ARNOLD, NESTOR FABIAN


#include <stdio.h>
#include <stdbool.h>


int multiplicar(int num1, int num2) {
    int total = 0;

    for (int i=0; i<num2; i++) {
        total += num1;
    }

    return total;
}


void productoria(int vector[], int* producto, int tam) {
    *producto = 1;

    for (int i=0; i<tam; i++) {
        *producto = multiplicar(*producto, vector[i]);
    }
}


int main() {
    int tamanio = -1;
    int prod = 0;

    printf("Productoria de elementos de un vector");

    while(tamanio < 1 || tamanio > 100) {
        printf("\nElija el tamanio del vector (debe estar entre 1 y 100 elementos): ");
        scanf("%d", &tamanio);
    }

    int lista_numeros[tamanio];

    for (int i=0; i<tamanio; i++) {
        printf("\nIngrese el elemento numero %d / %d del vector: ", i+1, tamanio);
        scanf("%d", &lista_numeros[i]);
    }

    productoria(lista_numeros, &prod, tamanio);

    printf("La productoria de todos los elementos del vector es:  %d", prod);

    return 0;
}
