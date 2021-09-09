/*
    Implementar la función void invertir(char *s) que invierte la cadena s (in-place).
*/


#include <stdio.h>
#include <string.h>


void invertir(char s[]) {
    char aux;
    char * destino; 
    const char * origen;

    //aun no funciona
    for (int i=0; i<strlen(s); i++) {
        destino = &s[i];
        origen = &s[strlen(s) - 1 - i];

        strcpy(&aux, destino);
        strcpy(destino, origen);
        strcpy(origen, &aux);
    }
    
   //strcpy(&s[0], &s[1]); //esto hace algo
}


int main() {
    char cadena[] = "ABcde FGH _5";
    invertir(cadena);
    printf("La cadena invertida es: %s", cadena);
    return 0;
}
