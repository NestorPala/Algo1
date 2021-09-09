#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define len(x) sizeof(x) / sizeof(x[0])


void hallar_max_min(int array[], int n, int* max, int* min) {
    bool min_max_iniciador = false;

    if (!min_max_iniciador) {
        *max = array[0];
        *min = array[0];
        min_max_iniciador = true;
    }

    for (int i=0; i<n; i++) {
        if (array[i] >= *max) {
            *max = array[i];
        }

        if (array[i] <= *min) {
            *min = array[i];
        }
    }
}


int main() {
    int numeros[] = {12, 90, -32, 9, 21382, 874, 0, 3232};
    int max = 0, min = 0;

    hallar_max_min(numeros, len(numeros), &max, &min);

    printf("El numero maximo del arreglo es: %d", max);
    printf("\nEl numero minimo del arreglo es: %d\n", min);

    return 0;
}
