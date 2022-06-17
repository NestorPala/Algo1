/*
    Usando las funciones printf y sizeof, escribir un programa que imprima el
    tamaño en bytes de cada uno de los siguientes tipos: bool, char, short, int, long, float, double,
    bool*, char*, short*, int*, long*, float*, double*.

    El programa debe mostrar la información con el siguiente formato:

    bool: 1
    char: 1
    short: 2
    . . .
*/


#include <stdio.h>
#include <stdbool.h>


int main() {
    printf("bool: %d\n", sizeof(bool));
    printf("char: %d\n", sizeof(char));
    printf("short: %d\n", sizeof(short));
    printf("int: %d\n", sizeof(int));
    printf("long: %d\n", sizeof(long));
    printf("float: %d\n", sizeof(float));
    printf("double: %d\n", sizeof(double));
    printf("bool*: %d\n", sizeof(bool*));
    printf("char*: %d\n", sizeof(char*));
    printf("short*: %d\n", sizeof(short*));
    printf("int*: %d\n", sizeof(int*));
    printf("long*: %d\n", sizeof(long*));
    printf("float*: %d\n", sizeof(float*));
    printf("double*: %d\n", sizeof(double*));
    
    return 0;
}
