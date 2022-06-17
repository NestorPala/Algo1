/*
    Escribir una función que reciba un número entero n y calcule el factorial de n. La función se puede escribir estar en forma iterativa o recursiva.
*/
#include <stdio.h>


unsigned long long factorial(int n) {
    if (n > 1) 
        return n * factorial(n - 1);
    else
        return 1;
}


int main() {
    int x = 16;
    printf("El factorial de %d es: %llu", x, factorial(x));
    return 0;
}
