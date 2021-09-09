/*
    Implementar la función unsigned int strlen(const char *s) que devuelve la
    longitud de la cadena s (sin contar el último caracter '\0'). La función se puede escribir estar en forma iterativa o recursiva.
*/


#include <stdio.h>


// DOC: Completar
unsigned int strlen_2(const char *s) {
    unsigned int tamanio_cadena = 0;

    if (*s != '\0') {
        tamanio_cadena++;
        return tamanio_cadena + strlen_2(s + 1);
    }
    else {
        return 0;
    }
}


int main() {
    char * cadena = "Hola, me llamo Juan Perez.";
    printf("El largo de la cadena es: %d", strlen_2(cadena));
    return 0;
}
