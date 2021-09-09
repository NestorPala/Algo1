#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*
char * strcat(char *dest, const char *src)
char * strcpy(char *dest, const char *src)
size_t strlen(const char *str)
*/


int main() {
    
    char nombre[50], apellido[50];

    printf("Ingrese su nombre:  ");
    scanf(" %s", &nombre);

    printf("Ingrese su apellido:  ");
    scanf(" %s", &apellido);

    strcat(nombre, " ");
    strcat(nombre, apellido);

    printf("Su nombre completo es: %s", nombre);
}
