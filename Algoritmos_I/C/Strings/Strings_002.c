#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*
char * strcat(char *dest, const char *src)
char * strcpy(char *dest, const char *src)
size_t strlen(const char *str)
*/


void juntar_palabras(const char * palabra1, const char * palabra2, char * frase_completa) {
    strcat(frase_completa, palabra1);
    strcat(frase_completa, " ");
    strcat(frase_completa, palabra2);
}


int main() {
    //ORIGEN
    const char palabra1[50] = "", palabra2[50] = "";

    //DESTINO
    char frase_completa[50] = "";

    printf("Ingrese palabra 1: ");
    scanf(" %s", &palabra1);

    printf("Ingrese palabra 2: ");
    scanf(" %s", &palabra2);

    juntar_palabras(palabra1, palabra2, frase_completa);

    printf("La frase completa es: %s", frase_completa);

    return 0;
}
