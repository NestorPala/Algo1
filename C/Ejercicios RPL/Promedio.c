/*
    
*/


#include <stdio.h>
#define len(x) (sizeof(x) / sizeof(x[0]))


float promedio(float numeros[], int n) {
    float acumulador = 0, pro = 0;

    for (int i=0; i<n; i++) {
        acumulador += numeros[i];
    }

    pro = acumulador / n;

    return pro;
}


int main() {
    float lista_numeros[] = {12, -13.54, 167, 9834, 0.17, 3678, 545, 0, -3243.143};

    printf("%.2f", promedio(lista_numeros, len(lista_numeros)));

    return 0;
}
