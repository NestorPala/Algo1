# include <stdio.h>


void modificar_numero(int *cajita) {
    *cajita = 21;
}

void modificar_numero_2(int *cajita2) {
    *cajita2 = 22;
}


int main() {
    int numero = 35;

    int *puntero = &numero;
    /*
    int *punt;
    punt = &numero;
    */

    printf("%d\n", numero);

    //Paso la dirección de memoria pelada, lo ataja el puntero del procedimiento
    modificar_numero(&numero);
    printf("%d\n", numero);

    //Paso la variable "punt", la cual, al ser un puntero, contiene como valor una dirección de memoria, 
    //la cual es atajada por el puntero del procedimiento
    modificar_numero_2(puntero);
    printf("%d", numero);

    return 0;
}


/*
int *puntero;

printf(&puntero) = imprime la dirección de memoria del puntero en sí
printf(puntero) = imprime la dirección de memoria de la variable a la que el puntero apunta
printf(*puntero) = imprime el contenido de la variable apuntada por el puntero (por ejemplo: 25)

*puntero = numero; //cambiamos el valor de la variable apuntada por el de "numero"
puntero = &numero; //al puntero le cambiamos la variable a la que apunta (usamos & para indicar dirección de memoria)
puntero = numero; //sirve para igualar la referencia de un puntero a la de otro puntero (como el de arriba pero con variable y no valor)

&puntero = numero; //no se puede
*/
